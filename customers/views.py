from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, Transfer
from django import forms

class NewUserForm(forms.Form):
    first = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'First Name'}), required=True)
    last = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Last Name'}), required=True)
    email = forms.EmailField(label="", widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Email'}), required=True)
    balance = forms.FloatField(min_value=0, initial=1000, label="", widget=forms.NumberInput(
        attrs={'class':'form-control', 'placeholder':'Balance'}), required=True)

# Create your views here.
def index(request):
    users = User.objects.all()
    return render(request, "customers/index.html", {
        "users": users
    })
    
def user(request, id):
    user = User.objects.get(pk=id)
    transfers = Transfer.objects.filter(Q(sender=user.id) | Q(receiver=user.id))
    return render(request, "customers/user.html", {
        "user": user,
        "transfers": transfers
    })

def users(request):
    users = User.objects.all()
    return render(request, "customers/users.html", {
        "users": users
    })

def addUser(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                first = form.cleaned_data['first'],
                last = form.cleaned_data['last'],
                email = form.cleaned_data["email"],
                balance = form.cleaned_data["balance"],
                time = request.POST["time"]
            )
            user.save()
            return HttpResponseRedirect(reverse("users"))
        else:
            return render(request, "customers/addUser.html", {
                "form": form,
                "time": "",
                "title": "Add new User",
                "required": "required",
                "action": "addUser"
            })
    return render(request, "customers/addUser.html", {
        "form": NewUserForm(),
        "time": "",
        "title": "Add new User",
        "required": "required",
        "action": "addUser"
    })

def editUser(request, id):
    user = User.objects.get(pk= id)
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.update_or_create(
                    pk = id,
                    defaults={'first': data["first"], 'last': data["last"],
                        'email': data["email"], 'balance': data["balance"]})
            return HttpResponseRedirect(reverse("users"))
        else:
            return render(request, "customers/addUser.html", {
                "form": form,
                "time": "",
                "title": "Edit User Data",
                "required": "",
                "action": "editUser",
                "id": user.id
            })
    form = NewUserForm(initial={
        'first': user.first,
        'last': user.last,
        'email': user.email,
        'balance': user.balance
    })
    return render(request, "customers/addUser.html", {
        "form": form,
        'time': user.time,
        "title": "Edit User Data",
        "required": "",
        "action": "editUser",
        "id": user.id
    })

def deleteUser(request, id):
    User.objects.get(pk=id).delete()
    return HttpResponseRedirect(reverse("users"))

def transactions(request):
    transfers = Transfer.objects.all()
    users = User.objects.all()
    return render(request, "customers/transactions.html", {
        "transfers": transfers,
        "users": users
    })
    
def addTransaction(request):
    list = User.objects.all()
    if request.method == "POST":
        data = request.POST
        if data["sender"] == data["receiver"]:
            return render(request, "customers/addTransaction.html",{
                "list": list,
                "message": "Sender & Receiver can't be the same person"
            })
        elif User.objects.get(pk=data["sender"]).balance < float(data["value"]):
            return render(request, "customers/addTransaction.html",{
                "list": list,
                "message": "Sender's balance doesn't have enough money"
            })
        else:
            transfer = Transfer()
            sender = User.objects.get(pk=data["sender"])
            sender.balance -= float(data["value"])
            sender.save()
            transfer.sender = sender
            receiver = User.objects.get(pk=data["receiver"])
            receiver.balance += float(data["value"])
            receiver.save()
            transfer.receiver = receiver
            transfer.value= data["value"]
            transfer.time = data["time"]
            transfer.save()
            return HttpResponseRedirect(reverse("transactions"))
    return render(request, "customers/addTransaction.html", {
        "list": list,
        "message": ""
    })

def search(request):
    if request.method == "POST":
        search = request.POST["user"]
        users = User.objects.filter(Q(first__contains=search) | Q(last__contains=search))
        return render(request, "customers/searchResults.html", {
            "users": users,
            "search": search
        })
    

from email import message
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, Transfer
from django import forms

class NewUserForm(forms.Form):
    first = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class':'first', 'placeholder':'First Name'}), required=True)
    last = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class':'last', 'placeholder':'Last Name'}), required=True)
    email = forms.EmailField(label="", widget=forms.EmailInput(
        attrs={'class':'email', 'placeholder':'Email'}), required=True)
    balance = forms.FloatField(min_value=0, initial=1000, label="", widget=forms.NumberInput(
        attrs={'class':'balance', 'placeholder':'Email'}), required=True)

# Create your views here.
def index(request):
    users = User.objects.all()
    return render(request, "customers/index.html", {
        "users": users
    })

def user(request, id):
    user = User.objects.get(pk=id)
    return render(request, "customers/user.html", {
        "user": user
    })

def addUser(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                first = form.cleaned_data['first'],
                last = form.cleaned_data['last'],
                email = form.cleaned_data["email"],
                balance = form.cleaned_data["balance"]
            )
            user.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "customers/addUser.html", {
                "form": form
            })
    return render(request, "customers/addUser.html", {
        "form": NewUserForm()
    })

def transactions(request):
    transfers = Transfer.objects.all()
    return render(request, "customers/transactions.html", {
        "transfers": transfers
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

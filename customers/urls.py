from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('adduser', views.addUser, name="addUser"),
    path('transactions', views.transactions, name="transactions"),
    path('addtransaction', views.addTransaction, name="addTransaction"),
    path('<str:id>', views.user, name="user"),
]
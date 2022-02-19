from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('users', views.users, name="users"),
    path('adduser', views.addUser, name="addUser"),
    path('edituser/<str:id>', views.editUser, name="editUser"),
    path('deleteuser/<str:id>', views.deleteUser, name="deleteUser"),
    path('transfers', views.transactions, name="transactions"),
    path('addtransfer', views.addTransaction, name="addTransaction"),
    path('search', views.search, name="search"),
    path('<str:id>', views.user, name="user"),
]
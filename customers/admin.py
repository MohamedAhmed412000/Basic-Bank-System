from django.contrib import admin
from .models import User, Transfer

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["first", "last", "email", "balance"]
    list_filter = ["first", "last"]

class TransferAdmin(admin.ModelAdmin):
    list_display = ["sender", "receiver", "value", "time"]
    list_filter = ["sender", "receiver"]

admin.site.register(User, UserAdmin)
admin.site.register(Transfer, TransferAdmin)
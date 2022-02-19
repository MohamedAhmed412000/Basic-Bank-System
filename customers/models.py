import uuid
from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    balance = models.FloatField()
    time = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return f"{self.first} {self.last}"

class Transfer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    value = models.FloatField()
    time = models.DateTimeField()

    def __str__(self):
        return f"User {self.sender} sends {self.value} LE to User {self.receiver}"

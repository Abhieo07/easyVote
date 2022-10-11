from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class CreateVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()

    def __str__(self):
        return self.user.username

class Option(models.Model):
    no_of_choices = models.IntegerField()
    discription = models.TextField(default='DISCRIPTIONS')

    def __int__(self):
        return self.no_of_choice

class Select(models.Model):
    opt = models.CharField(max_length=20)

    def __str__(self):
        return self.opt
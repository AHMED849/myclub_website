# members/models.py

from django.db import models
from django.contrib.auth.models import User

class Login(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Login for {self.user.username}"

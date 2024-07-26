from django.db import models
from django.contrib.auth.models import User





class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    PARENT_STATUS_CHOICES = [
        ('single', 'Single'),
        ('none', 'None'),
        ('both', 'Both'),
    ]
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    registration_number = models.CharField(max_length=20)
    dob = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    course = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    parent_status = models.CharField(max_length=6, choices=PARENT_STATUS_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username



class Payment(models.Model):
    id = models.BigAutoField(primary_key=True)
    amount = models.IntegerField()
    def __str__(self):
        return f"Payment {self.reference_no} for {self.student}"

class Login(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logins')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Login for {self.user.username}"


class userlogincount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='login_counts')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Login count for {self.user.username}"

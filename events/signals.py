
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import userlogincount
from django.utils import timezone
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Student


@receiver(user_logged_in)
def update_login_time(sender, request, user, **kwargs):
    login_count, created = userlogincount.objects.get_or_create(user=user)
    login_count.login_time = timezone.now()
    login_count.save()

@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_student_profile(sender, instance, **kwargs):
    instance.student.save()
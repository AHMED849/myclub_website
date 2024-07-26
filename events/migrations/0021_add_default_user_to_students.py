from django.db import migrations
from django.conf import settings
from django.contrib.auth.models import User

def add_default_user(apps, schema_editor):
    Student = apps.get_model('events', 'Student')
    User = apps.get_model('auth', 'User')

    # Create a default user if it doesn't already exist
    default_user, created = User.objects.get_or_create(
        username='default_user', 
        defaults={'email': 'default@example.com', 'password': 'default_password'}
    )

    # Assign the default user to any student without a user
    for student in Student.objects.filter(user_id__isnull=True):
        student.user = default_user
        student.save()

class Migration(migrations.Migration):

    dependencies = [
        ('events', '0018_remove_payment_date_remove_payment_reference_no_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RunPython(add_default_user),
    ]

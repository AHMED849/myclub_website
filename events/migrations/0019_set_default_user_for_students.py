# migrations/0019_set_default_user_for_students.py

from django.db import migrations, models
from django.conf import settings
from django.contrib.auth.models import User

def set_default_user(apps, schema_editor):
    Student = apps.get_model('events', 'Student')
    User = apps.get_model(settings.AUTH_USER_MODEL)

    for student in Student.objects.all():
        if student.user_id is None:
            new_user = User.objects.create(username=f'default_user_{student.id}')
            student.user = new_user
            student.save()

class Migration(migrations.Migration):

    dependencies = [
        ('events', '0018_remove_payment_date_remove_payment_reference_no_and_more'),
    ]

    operations = [
        migrations.RunPython(set_default_user),
    ]

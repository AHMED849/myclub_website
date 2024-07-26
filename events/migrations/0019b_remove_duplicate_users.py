# migrations/0019b_remove_duplicate_users.py

from django.db import migrations, models
from django.conf import settings
from django.db.models import Count

def remove_duplicate_users(apps, schema_editor):
    Student = apps.get_model('events', 'Student')
    User = apps.get_model(settings.AUTH_USER_MODEL)

    # Find all students grouped by user_id having count more than 1 (i.e., duplicates)
    duplicates = (
        Student.objects.values('user_id')
        .annotate(user_count=Count('user_id'))
        .filter(user_count__gt=1)
    )

    for duplicate in duplicates:
        students = Student.objects.filter(user_id=duplicate['user_id'])
        # Keep the first student, remove others
        for student in students[1:]:
            student.user = None  # Remove user reference
            student.save()

class Migration(migrations.Migration):

    dependencies = [
        ('events', '0019_set_default_user_for_students'),
    ]

    operations = [
        migrations.RunPython(remove_duplicate_users),
    ]

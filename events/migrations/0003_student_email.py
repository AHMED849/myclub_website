# Generated by Django 5.0.6 on 2024-05-31 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_student_dob_alter_payment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-31 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

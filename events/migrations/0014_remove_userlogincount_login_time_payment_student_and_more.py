# Generated by Django 5.0.6 on 2024-07-01 09:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20240701_1213'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlogincount',
            name='login_time',
        ),
        migrations.AddField(
            model_name='payment',
            name='student',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='login',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logins', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userlogincount',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='login_counts', to=settings.AUTH_USER_MODEL),
        ),
    ]

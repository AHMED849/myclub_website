from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings

class Migration(migrations.Migration):

    dependencies = [
        ('events', '0022_merge_20240702_1703'),  # Update with your actual previous migration
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.CASCADE),
        ),
    ]

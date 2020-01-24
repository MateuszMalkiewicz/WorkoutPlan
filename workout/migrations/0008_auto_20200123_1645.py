# Generated by Django 3.0.2 on 2020-01-23 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workout', '0007_auto_20191129_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercisemodel',
            name='user',
        ),
        migrations.AddField(
            model_name='loadmodel',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
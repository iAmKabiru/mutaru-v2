# Generated by Django 2.2.7 on 2019-11-07 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0023_auto_20191107_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='submittedBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]

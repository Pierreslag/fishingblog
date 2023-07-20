# Generated by Django 3.2.20 on 2023-07-20 19:15

from django.db import migrations, models
import django.utils.timezone


def set_default_created_on(apps, schema_editor):
    ContactMessage = apps.get_model('blog', 'ContactMessage')
    ContactMessage.objects.all().update(created_on=django.utils.timezone.now())


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_contactmessage'),
    ]

    operations = [
        migrations.RunPython(set_default_created_on),
    ]
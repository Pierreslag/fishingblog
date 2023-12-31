# Generated by Django 3.2.20 on 2023-07-20 19:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_contactmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]

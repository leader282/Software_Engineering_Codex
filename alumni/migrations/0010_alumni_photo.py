# Generated by Django 4.1.7 on 2023-04-07 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0009_chat_isactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
    ]
# Generated by Django 4.1.7 on 2023-04-07 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadmin', '0004_cadmin_ishiring'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadmin',
            name='isverified',
            field=models.BooleanField(default=False),
        ),
    ]
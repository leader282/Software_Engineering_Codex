# Generated by Django 4.1.7 on 2023-03-24 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=1000)),
                ('roll', models.CharField(max_length=9)),
                ('phone', models.IntegerField(max_length=10)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]
# Generated by Django 4.1.7 on 2023-04-03 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_name', models.CharField(max_length=1000)),
                ('a_email', models.EmailField(max_length=100)),
                ('date_joined', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date of Joining')),
                ('a_contactno', models.IntegerField(blank=True, null=True)),
                ('a_profile', models.CharField(choices=[('s', 'SOFTWARE'), ('d', 'DATA'), ('f', 'FINANCE'), ('q', 'QUANT')], default='s', max_length=4)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

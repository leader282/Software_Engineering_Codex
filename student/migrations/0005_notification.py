# Generated by Django 4.1.7 on 2023-04-08 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_remove_student_cv_student_cv_d_student_cv_f_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=10000000)),
            ],
        ),
    ]
# Generated by Django 3.1.5 on 2023-02-07 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_employeruser_hasjobber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employercomplain',
            name='job',
        ),
        migrations.RemoveField(
            model_name='jobbercomplain',
            name='job',
        ),
    ]

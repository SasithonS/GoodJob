# Generated by Django 3.1.5 on 2023-02-02 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_applyjob'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyjob',
            name='check_apply',
            field=models.BooleanField(default=False, verbose_name='สมัครสำเร็จ'),
        ),
    ]
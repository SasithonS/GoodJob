# Generated by Django 3.1.5 on 2023-02-05 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_job_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobberuser',
            name='hasjob',
            field=models.BooleanField(default=False, verbose_name='มีงาน'),
        ),
    ]

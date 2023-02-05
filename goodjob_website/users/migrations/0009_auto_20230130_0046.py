# Generated by Django 3.1.5 on 2023-01-29 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_jobuser_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobuser',
            name='address',
            field=models.CharField(blank=True, max_length=100, verbose_name='ที่อยู่'),
        ),
        migrations.AlterField(
            model_name='jobuser',
            name='location',
            field=models.CharField(blank=True, max_length=100, verbose_name='ที่ตั้ง'),
        ),
    ]
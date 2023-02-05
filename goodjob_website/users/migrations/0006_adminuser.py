# Generated by Django 3.1.5 on 2023-01-29 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0005_auto_20230127_0513'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user', verbose_name='บัญชีผู้ใช้')),
                ('name', models.CharField(max_length=100, verbose_name='ชื่อ-สกุล')),
                ('email', models.EmailField(max_length=100, verbose_name='อีเมล')),
                ('picture', models.FileField(blank=True, null=True, upload_to='jobs/static/jobs/images/Admin/', verbose_name='รูปภาพ')),
            ],
        ),
    ]
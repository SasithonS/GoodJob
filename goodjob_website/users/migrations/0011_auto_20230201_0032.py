# Generated by Django 3.1.5 on 2023-01-31 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20230131_2359'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployerCheck',
            fields=[
                ('employer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.employeruser', verbose_name='ผู้จ้างงาน')),
                ('identity_pic', models.FileField(blank=True, null=True, upload_to='jobs/static/jobs/images/identity/Employer/', verbose_name='หลักฐานยืนยันตัวตน')),
                ('check_emp', models.BooleanField(default=False, verbose_name='ตรวจสอบ')),
            ],
        ),
        migrations.CreateModel(
            name='JobberCheck',
            fields=[
                ('jobber', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.jobberuser', verbose_name='ผู้หางาน')),
                ('identity_pic', models.FileField(blank=True, null=True, upload_to='jobs/static/jobs/images/identity/Employer/', verbose_name='หลักฐานยืนยันตัวตน')),
                ('check_jobber', models.BooleanField(default=False, verbose_name='ตรวจสอบ')),
            ],
        ),
        migrations.RemoveField(
            model_name='employeruser',
            name='check',
        ),
        migrations.RemoveField(
            model_name='jobberuser',
            name='check',
        ),
        migrations.AlterField(
            model_name='jobuser',
            name='jobber',
            field=models.ManyToManyField(blank=True, to='users.JobberUser', verbose_name='ผู้สมัคร'),
        ),
    ]

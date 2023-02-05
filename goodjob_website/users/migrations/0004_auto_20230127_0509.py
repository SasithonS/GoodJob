# Generated by Django 3.1.5 on 2023-01-26 22:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0019_auto_20230115_1452'),
        ('users', '0003_auto_20230127_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobberuser',
            name='address',
            field=models.CharField(blank=True, default='-', max_length=100, null=True, verbose_name='ที่อยู่'),
        ),
        migrations.AlterField(
            model_name='jobberuser',
            name='education',
            field=models.ForeignKey(blank=True, default='-', null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.education', verbose_name='ระดับการศึกษา'),
        ),
        migrations.AlterField(
            model_name='jobberuser',
            name='gender',
            field=models.ForeignKey(blank=True, default='-', null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.gender'),
        ),
        migrations.AlterField(
            model_name='jobberuser',
            name='location',
            field=models.CharField(blank=True, default='-', max_length=100, null=True, verbose_name='ที่ตั้ง'),
        ),
        migrations.AlterField(
            model_name='jobberuser',
            name='phone',
            field=models.CharField(default='-', max_length=100, verbose_name='เบอร์โทร'),
        ),
        migrations.AlterField(
            model_name='jobberuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='บัญชีผู้ใช้'),
        ),
    ]
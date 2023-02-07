from django.db import models
from jobs.models import *
from django.contrib.auth.models import User
# Create your models here.


class EmployerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,verbose_name='บัญชีผู้ใช้')
    name = models.CharField('ชื่อองค์กร/ร้านค้า',max_length=100)
    emp_name = models.CharField('ชื่อผู้จ้าง',max_length=100, null=True, blank=True,)
    email = models.EmailField('อีเมล',max_length=100)
    phone = models.CharField('เบอร์โทร',max_length=100,null=True, blank=True,)
    address = models.CharField('ที่อยู่',max_length=100)
    province = models.ForeignKey(Province,on_delete=models.CASCADE,verbose_name='จังหวัด')
    location = models.CharField('ที่ตั้ง',max_length=100, null=True, blank=True,)
    picture = models.FileField('รูปภาพ',null=True, blank=True, upload_to='jobs/static/jobs/images/Employer/')

    def __str__(self):
        return self.name

class JobberUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,verbose_name='บัญชีผู้ใช้')
    name = models.CharField('ชื่อ-สกุล',max_length=100)
    email = models.EmailField('อีเมล',max_length=100)
    phone = models.CharField('เบอร์โทร',max_length=100)
    address = models.CharField('ที่อยู่',max_length=100,null=True,blank=True)
    location = models.CharField('ที่ตั้ง',max_length=100,null=True,blank=True)
    age = models.IntegerField('อายุ',default=0,null=True, blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE,null=True, blank=True)
    province = models.ForeignKey(Province,on_delete=models.CASCADE,verbose_name='จังหวัด',null=True,blank=True)
    education = models.ForeignKey(Education, on_delete=models.CASCADE,verbose_name='ระดับการศึกษา',null=True, blank=True)
    picture = models.FileField('รูปภาพ',null=True, blank=True, upload_to='jobs/static/jobs/images/Jobber/')
    hasjob = models.BooleanField('มีงาน',default=False)

    
    def __str__(self):
        return self.name

class AdminUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,verbose_name='บัญชีผู้ใช้')
    name = models.CharField('ชื่อ-สกุล',max_length=100)
    email = models.EmailField('อีเมล',max_length=100)
    picture = models.FileField('รูปภาพ',null=True, blank=True, upload_to='jobs/static/jobs/images/Admin/')

    def __str__(self):
        return self.name

class Job(models.Model):
    name = models.CharField('ชื่องาน',max_length=100)
    description = models.TextField('รายละเอียดงาน',blank=True)
    address = models.CharField('ที่อยู่',max_length=100,blank=True)
    location = models.CharField('ที่ตั้ง',max_length=100,blank=True)
    phone = models.CharField('เบอร์โทร',max_length=100)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE,verbose_name='เพศ')
    emp_name = models.ForeignKey(EmployerUser, blank=True, null=True, on_delete=models.CASCADE,verbose_name='ผู้จ้างงาน')
    province = models.ForeignKey(Province,on_delete=models.CASCADE,verbose_name='จังหวัด')
    pay = models.ForeignKey(Pay,on_delete=models.CASCADE,verbose_name='ค่าตอบแทน')
    jobber = models.IntegerField('จำนวนผู้สมัคร',default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    picture = models.FileField('รูปภาพ',null=True, blank=True, upload_to='jobs/static/jobs/images/Job/')
    apply = models.BooleanField('มีการจ้างงาน',default=False)
    
    def __str__(self):
        return str(self.name)

class JobberCheck(models.Model):
    jobber = models.OneToOneField(JobberUser, on_delete=models.CASCADE, primary_key=True,verbose_name='ผู้หางาน')
    identity_pic = models.FileField('หลักฐานยืนยันตัวตน',null=True, blank=True, upload_to='jobs/static/jobs/images/identity/Employer/')
    check_jobber = models.BooleanField('ตรวจสอบ',default=False)

class EmployerCheck(models.Model):
    employer = models.OneToOneField(EmployerUser, on_delete=models.CASCADE, primary_key=True,verbose_name='ผู้จ้างงาน')
    check_emp = models.BooleanField('ตรวจสอบ',default=False)
    identity_pic = models.FileField('หลักฐานยืนยันตัวตน',null=True, blank=True, upload_to='jobs/static/jobs/images/identity/Employer/')

class ApplyJob(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE,verbose_name='ชื่องาน')
    jobber = models.ForeignKey(JobberUser, on_delete=models.CASCADE, verbose_name='ผู้สมัคร')
    emp_name = models.ForeignKey(EmployerUser, on_delete=models.CASCADE,verbose_name='ผู้จ้างงาน')
    apply_date = models.DateTimeField('วันที่สมัคร',auto_now_add=True)
    check_apply = models.BooleanField('จ้างงาน',default=False)
    picture = models.FileField('รูปภาพ',null=True, blank=True, upload_to='jobs/static/jobs/images/ApplyJob/')

    def __str__(self):
        return str(self.job)


class JobberComplain(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE,verbose_name='ชื่องาน')
    jobber = models.ForeignKey(JobberUser, on_delete=models.CASCADE, verbose_name='ผู้สมัคร')
    emp_name = models.ForeignKey(EmployerUser, on_delete=models.CASCADE,verbose_name='ผู้จ้างงาน')
    subject = models.ForeignKey(JobberSubjectComplain, on_delete=models.CASCADE, verbose_name='หัวข้อร้องเรียน')
    description = models.TextField('รายละเอียดงาน',blank=True,max_length=256)
    complain_date = models.DateTimeField('วันที่ร้องเรียน', auto_now_add=True)
    status = models.BooleanField('ได้รับคำร้อง',default=False)


class EmployerComplain(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE,verbose_name='ชื่องาน')
    jobber = models.ForeignKey(JobberUser, on_delete=models.CASCADE, verbose_name='ผู้สมัคร')
    emp_name = models.ForeignKey(EmployerUser, on_delete=models.CASCADE,verbose_name='ผู้จ้างงาน')
    subject = models.ForeignKey(EmployerSubjectComplain, on_delete=models.CASCADE, verbose_name='หัวข้อร้องเรียน')
    description = models.TextField('รายละเอียดงาน',blank=True,max_length=256)
    complain_date = models.DateTimeField('วันที่ร้องเรียน', auto_now_add=True)
    status = models.BooleanField('ได้รับคำร้อง',default=False)

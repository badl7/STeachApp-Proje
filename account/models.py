from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings
from autoslug import AutoSlugField

# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Student')
    name=models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=25)
    slug = AutoSlugField(populate_from = 'user', unique=True)
    student_profile_pic = models.ImageField(upload_to="avatar/student_profile_pic",blank=True, null=True)
    olus_tarih = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    
    def get_absolute_url(self):
        return reverse('#',kwargs={'pk':self.pk})
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'studentuser'
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['olus_tarih']

class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='Teacher')
    name = models.CharField(max_length=250)
    subject_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    slug = AutoSlugField(populate_from = 'user', unique=True)
    teacher_profile_pic = models.ImageField(upload_to="avatar/teacher_profile_pic",blank=True, null=True)
    class_students = models.ManyToManyField(Student,through="StudentsInClass")
    olus_tarih = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    
    def get_absolute_url(self):
        return reverse('#',kwargs={'pk':self.pk})
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'teacheruser'
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
        ordering = ['olus_tarih']
    


class StudentsInClass(models.Model):
    teacher = models.ForeignKey(Teacher,related_name="s_teacher",on_delete=models.CASCADE)
    student = models.ForeignKey(Student,related_name="user_student_name",on_delete=models.CASCADE)

    def __str__(self):
        return self.student.name

    class Meta:
        unique_together = ('teacher','student')

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["user"]
        verbose_name_plural = "Users"

    def __str__(self):
        return self.user.username

class Course(models.Model):
    name = models.CharField('name of course', max_length = 30)
    maxLength =  models.IntegerField()
    minLength = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["user"]
        verbose_name_plural = "Students"

    def __str__(self):
        return self.user.username





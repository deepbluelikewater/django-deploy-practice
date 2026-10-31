from django.db import models

# Create your models here.


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    student_email = models.CharField(max_length=100)
    student_password = models.CharField(max_length=100)

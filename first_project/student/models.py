from django.db import models

# Create your models here.
class module_1(models.Model):
    roll_number=models.CharField(max_length=2)
    student_name=models.CharField(max_length=50)
    student_class=models.CharField(max_length=10)
    student_section=models.CharField(max_length=1)
    student_email=models.EmailField()
    phone_number=models.IntegerField()
    subject=models.CharField(max_length=20)
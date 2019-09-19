from django.db import models

from datetime import datetime

# Create your models here.
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Department Name',max_length=100)

    def __str__(self):
            return self.name

    class Meta:
        db_table = "departments"
        ordering = ('name',)

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Employee Name", max_length=100)
    email = models.EmailField("Email Address", max_length=100)
    dob = models.DateTimeField("Date of Birth",help_text="Format: yyyy/mm/dd")
    salary = models.FloatField("Monthly Salary")
    photo = models.FileField(upload_to="myimage", default='blank.png',blank=True)
    department = models.ForeignKey(Department,default=' ',on_delete=models.CASCADE)
	#department = models.ForeignKey(Department,default='Admin',blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "employees"

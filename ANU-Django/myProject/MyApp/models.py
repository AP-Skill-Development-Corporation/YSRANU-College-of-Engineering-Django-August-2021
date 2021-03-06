from django.db import models

# Create your models here.

class Student(models.Model):
	name=models.CharField(max_length=30)
	rollnum=models.CharField(max_length=30)
	age=models.IntegerField()
	mobile=models.CharField(max_length=10)
	email=models.EmailField(max_length=30)
	address=models.TextField()


	def __str__(self):
		return self.name+' '+self.email

class Register(models.Model):
	genders=[('Female','Female'),
			  ('Male','Male')
	]
	branches=[('Select','Select'),('CSE','CSE'),('ECE','ECE'),('EEE','EEE'),('MECH','MECH')]
	name=models.CharField(max_length=30)
	mobile_no=models.CharField(max_length=10)
	age=models.IntegerField()
	gender=models.CharField(max_length=10,choices=genders,null=True)
	branch=models.CharField(max_length=10,choices=branches,null=True)
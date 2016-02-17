from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class College(models.Model):
	collegeName = models.CharField(max_length=100)
	addressLine1 = models.TextField()
	addressLine2 = models.TextField()
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	pincode = models.IntegerField()
	contactNo = models.IntegerField()
	landlineNo = models.IntegerField()

class Department(models.Model):
	departmentName = models.CharField(max_length=50)
	departmentCode = models.IntegerField()

	FE = 0
	SE = 1
	TE = 2
	BE = 3

	YEARCHOICES = ((FE,"First Year"),(SE,"Second Year"),(TE,"Third Year"),(BE,"Final Year"))
	optionType = models.IntegerField(choices=YEARCHOICES)

	FIRST = 0
	SECOND = 1
	THIRD = 2
	FOURTH = 3
	FIFTH = 4
	SIXTH = 5
	SEVENTH = 6
	FINAL = 7

	SEMESTERCHOICES = ((FIRST,"FIRST"),(SECOND,"SECOND"),(THIRD,"THIRD"),(FOURTH,"FOURTH"),(FIFTH,"FIFTH")
		,(SIXTH,"SIXTH"),(SEVENTH,"SEVENTH"),(FINAL,"FINAL"))
	optionType = models.IntegerField(choices=SEMESTERCHOICES)

class Student(models.Model):
	firstName = models.CharField(max_length=20)
	middleName = models.CharField(max_length=20)
	lastName = models.CharField(max_length=20)
	user = models.ForeignKey(User)

class Subjects(models.Model):
	subjectName = models.CharField(max_length=50)
	subjectCode = models.IntegerField()
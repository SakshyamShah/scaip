from __future__ import unicode_literals

from django.db import models

# Create your models here.

# get user report
#class Catagory(models.Model):
#	name = models.CharField(max_length = 100)

# get location
#class Location(models.Model):
#	name = models.CharField(max_length = 100)

# get name of trafficker(optional)
#class Trafficker_name(models.Model):
#	name = models.CharField(max_length = 100)

# get Description
#class Issue_desc(models.Model):
#	description = models.CharField(max_length = 200)

# get user report
class Report_Data(models.Model):
	Child_Labour = 'Child-Labour'
	Sex_Traffick = 'Sex-Traffick'
	catagory_choices = (
		(Child_Labour, 'Child-labour'),
		(Sex_Traffick, 'Sex-traffick')
		)
	Catagory = models.CharField(max_length = 100, choices=catagory_choices)
	report_location = models.CharField(max_length = 100)
	trafficker_name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 200)

from django.db import models

# Create your models here
class Target(models.Model):
	name = models.CharField(max_length=30)
	time_allownace = models.CharField(max_length=30)
	comment=models.CharField(max_length=5000)
	status = models.CharField(max_length=30)
	user = models.CharField(max_length=30)
	def __unicode__(self):
		return self.name
	

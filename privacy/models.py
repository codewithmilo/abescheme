from django.db import models

class Policy(models.Model):
	name = models.CharField(max_length=100)
	viewers = models.CharField(max_length=100)
	display_length = models.CharField(max_length=100)
	deleted_length = models.CharField(max_length=100)
	data_use = models.CharField(max_length=100)
	tracking = models.CharField(max_length=100)
	gps_loc = models.CharField(max_length=100)
	def __unicode__(self):
		return self.name
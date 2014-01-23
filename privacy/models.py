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

class PostedData(models.Model):
	p_id = models.CharField(max_length=10)
	status = models.CharField(max_length=200)
	posted = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.status
from django.db import models

class Policy(models.Model):
	name = models.CharField(max_length=100)
	policy = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name

class PostedData(models.Model):
	p_id = models.CharField(max_length=10)
	status = models.CharField(max_length=5000)
	posted = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.status

class Authority(models.Model):
	app_name = models.CharField(max_length=100)
	attr_list = models.CharField(max_length=1000)
	p_key = models.CharField(max_length=3000)
	d_key = models.CharField(max_length=3000)
	def __unicode__(self):
		return self.app_name

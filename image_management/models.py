from __future__ import unicode_literals

from django.db import models

class Photo(models.Model):
	file_name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='photos', max_length=255)

	def save(self, *args, **kwargs):
		import pdb; pdb.set_trace()
# Create your models here.

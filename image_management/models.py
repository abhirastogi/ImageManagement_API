from __future__ import unicode_literals

from django.db import models

class Photo(models.Model):
	file_name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='photos', max_length=255)

# Create your models here.

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Weight(models.Model):
	"""Weight"""
	date = models.CharField('Date',max_length=255)
	weight = models.IntegerField('Weight',blank=True)

	def __str__(self):
		return self.date

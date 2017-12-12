# -*- coding: utf-8 -*-

from django.db import models

class Apoio(models.Model):
	nome = models.CharField(
		max_length=40,
		blank=False
	)

	cel = models.CharField(
		max_length=10,
		blank=True,
		unique=False
	)
	email = models.CharField(
		max_length=30,
		blank=True,
		unique=False
	)

	def __unicode__(self):
		return self.nome

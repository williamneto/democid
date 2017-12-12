# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from models import Apoio

class AssineForm(ModelForm):
	class Meta:
		model = Apoio
		fields = ['nome', 'cel', 'email']

		labels = {
			"nome": "Nome",
		}

		error_messages = {
			"nome": {
				"required": "Preencha seu nome"
			},
		}

	def clean(self):
		cleaned_data = super(AssineForm, self).clean()
		nome = cleaned_data.get('nome')

		try:
			existe = Apoio.objects.get(
				nome=nome,
			)
			raise forms.ValidationError("Sua assinatura já foi registrado anteriormente")
		except Apoio.DoesNotExist:
			pass

		return cleaned_data
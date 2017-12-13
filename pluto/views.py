# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from forms import AssineForm
from models import Apoio

class IndexView(TemplateView):
	template_name = "index.html"

	def get_context_data(self, *args, **kwargs):
		ctx = super(IndexView, self).get_context_data(*args, **kwargs)

		ctx['count_apoios'] = len(Apoio.objects.all())

		return ctx

class AssineView(FormView):
	template_name = "assine.html"
	form_class = AssineForm
	success_url = "/fim/"

	def form_valid(self, form):
		apoio  = form.save(commit=False)
		apoio.save()

		return super(AssineView,self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		ctx = super(AssineView, self).get_context_data(*args, **kwargs)

		ctx['count_apoios'] = len(Apoio.objects.all())

		return ctx

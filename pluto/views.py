# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from forms import AssineForm

class IndexView(TemplateView):
	template_name = "index.html"

class AssineView(FormView):
	template_name = "assine.html"
	form_class = AssineForm
	success_url = "/fim/"

	def form_valid(self, form):
		apoio  = form.save(commit=False)
		apoio.save()

		return super(AssineView,self).form_valid(form)

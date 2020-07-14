# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy

from .forms import MirrorCalcForm


class MirrorCalcView(FormView):
    form_class = MirrorCalcForm
    template_name = 'calc.html'
    success_url = reverse_lazy('calcapp:calc')

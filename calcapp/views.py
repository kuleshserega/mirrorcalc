from django.shortcuts import render

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generics import FormView

from . import MirrorCalcForm


class MirrorCalcView(FormView):
    form_class = MirrorCalcForm

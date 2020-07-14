# -*- coding: utf-8 -*-
from django import forms


class MirrorCalcForm(forms.Form):
    height = forms.FloatField(label='Высота', max_length=10)
    width = forms.FloatField(label='Ширина', max_length=10)

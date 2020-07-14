# -*- coding: utf-8 -*-
from django import forms


class MirrorCalcForm(forms.Form):
    height = forms.FloatField(label='Высота')
    width = forms.FloatField(label='Ширина')

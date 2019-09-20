#!/usr/bin/env  python3
# -*- coding: UTF-8 -*-
from django import forms
from django.core.exceptions import ValidationError

from app import models

class HostModelForms(forms.ModelForm):
    class Meta:
        model = models.Host
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(HostModelForms, self).__init__(*args, **kwargs)
        # 统一给ModelForm生成字段添加样式
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

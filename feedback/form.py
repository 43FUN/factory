# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from feedback.models import Feedback


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'phone', 'text', 'file']

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={
            'class': 'feedback__text',
            'placeholder': 'Введите Ваше имя'})
        self.fields['email'].widget = forms.TextInput(attrs={
            'class': 'feedback__text',
            'placeholder': 'Ваш email'})
        self.fields['phone'].widget = forms.TextInput(attrs={
            'class': 'feedback__text',
            'placeholder': 'Ваш телефон'})
        self.fields['text'].widget = forms.Textarea(attrs={
            'class': 'feedback__text',
            'rows': '6'})
        self.fields['file'].widget = forms.FileInput(attrs={
            'class': 'btn btn_green feedback__attach'})
        self.fields['file'].required = False




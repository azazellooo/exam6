from django import forms
from django.forms import widgets


class NoteForm(forms.Form):
    name = forms.CharField(max_length=120, required=True, label='Имя')
    email = forms.EmailField(required=True, label='Email')
    text = forms.CharField(max_length=1500, required=True, widget=widgets.Textarea, label='Текст')

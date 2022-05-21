from django import forms


class TagForm(forms.Form):
    label = forms.CharField(max_length=225)
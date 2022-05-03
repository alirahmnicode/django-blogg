from django import forms
from .models import Article , Tag    


class AddArticleForm(forms.Form):
    title = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
    tags = forms.CharField(max_length=1000)



class EditArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title' , 'body' , 'image' , 'tags')
       

class AddTag(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
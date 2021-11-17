from django import forms

from .models import Article



class ArticleCreateForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput( attrs={ 'placeholder': 'Article Title'} ))
    content = forms.CharField( widget=forms.Textarea( 
        attrs={ 
            'rows': 20,
            'cols': 120,
            'placeholder': 'Content Goes here'
         }
     ) )
    active = forms.BooleanField( widget= forms.CheckboxInput( attrs={ 'checked': False }))

    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
        ]




class RawArticleForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput( attrs={ 'placeholder': 'Article Title'} ))
    content = forms.CharField( widget=forms.Textarea( 
        attrs={ 
            'rows': 20,
            'cols': 300,
            'placeholder': 'Content Goes here'
         }
     ) )
    active = forms.BooleanField( widget= forms.CheckboxInput( attrs={ 'checked': False }))
from django import forms
from .models import Article

class ArticleModelForm(forms.ModelForm): # a model form
    title   = forms.CharField(
                widget=forms.TextInput(
                    attrs={
                        'placeholder': 'Title of the article',
                    }
                )
            )
    # date    = forms.DateField()
    content = forms.CharField(
                required=False,
                widget=forms.Textarea(
                    attrs={
                        'rows':20,
                        'cols':120,
                        'placeholder': 'Write the article here...',
                    }
                )
            )
    active  = forms.BooleanField(required=False)
    
    class Meta:
        model = Article
        readonly_fields = ['date']
        fields = [
                'title',
                'content',
                'active',
            ]
            
    def clean_title(self,*args,**kwargs):
        title=self.cleaned_data.get('title')
        if not ' ' in title:
            raise forms.ValidationError('Invalid title: title must contain at leat two words.')
        else:
            return title

# class RawArticleForm(forms.Form): # a raw form
#     title   = forms.CharField(
#                 widget=forms.TextInput(
#                     attrs={
#                         'placeholder': 'Title of the article',
#                     }
#                 )
#             )
#     date    = forms.DateField()
#     content = forms.CharField(
#                 required=False,
#                 widget=forms.Textarea(
#                     attrs={
#                         'rows':20,
#                         'cols':120,
#                         'placeholder': 'Write the article here...',
#                     }
#                 )
#             )
#     active  = forms.BooleanField(required=False)
    
#     def clean_title(self,*args,**kwargs):
#         title=self.cleaned_data.get('title')
#         if not ' ' in title:
#             raise forms.ValidationError('Invalid title: title must contain at leat two words.')
#         else:
#             return title
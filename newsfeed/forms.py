from django import forms
from django.forms import ModelForm
from .models import Blog,Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','caption','picture','user']
        widgets={
            'user':forms.HiddenInput()
        }
    def __init__(self,*args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self) 
        self.helper.add_input(Submit('submit', 'POST'))
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['comment','post','user']
        widgets={
            'user':forms.HiddenInput(),
            'post':forms.HiddenInput()
        }
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self) 
        self.helper.add_input(Submit('submit', 'Submit'))
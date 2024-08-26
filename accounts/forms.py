from django.forms import ModelForm
from .models import CustomUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth import get_user_model
CustomUser = get_user_model()
class update_user(ModelForm):
    class Meta:
        model=CustomUser
        fields=['phone_number','user_bio','user_profile_image']
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self) 
        self.helper.add_input(Submit('submit', 'UPDATE'))
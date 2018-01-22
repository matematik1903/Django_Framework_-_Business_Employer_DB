from django import forms
from User_and_vacan.models import *

class users_jobForm(forms.ModelForm):

    class Meta:
        model = ProductImage
        exclude = [""]
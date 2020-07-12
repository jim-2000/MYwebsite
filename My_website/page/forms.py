from django import forms
from .models import massage

# write your form 

class getMassage(forms.ModelForm):
     class Meta:
        model = massage
        fields = '__all__'
        
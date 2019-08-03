from .models import Profiles,Projects,Reviews
from django import forms
from django.forms import ModelForm, Textarea, IntegerField

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['image','details','url']
        exclude = ['profile','posted']
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        exclude = ['posted','project','user']
        
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ['image','bio','contact']
        exclude = ['user']
        
class RatemeSubscriptionForm(forms.ModelForm):
    name = forms.CharField(label='Username',max_length=30)
    email = forms.EmailField(label='Email')
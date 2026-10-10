from django import forms
from django.contrib.auth.models import User
from .models import Profile, Preference

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'dob', 'gender', 'mobile', 'location', 'education', 'occupation', 'income', 'hobbies', 'about', 'photo']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

class PreferenceForm(forms.ModelForm):
    class Meta:
        model = Preference
        fields = ['preferred_gender', 'min_age', 'max_age', 'preferred_location', 'preferred_education']

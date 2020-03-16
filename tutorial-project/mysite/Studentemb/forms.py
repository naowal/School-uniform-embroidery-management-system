from django import forms
from .models import StudentEmbInfo, user


class StudentEmbInfoForm(forms.ModelForm):
    class Meta:
        model = StudentEmbInfo
        fields = ['name', 'firstname', 'lastname', 'schoolname', 'moreinfo', 'status', 'color', 'create_by', 'price_baht']


class userForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['name']



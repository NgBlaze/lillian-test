from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput
from .models import Profile
from django.forms import ModelForm
from .models import Contact
from dataclasses import fields

# Create your forms here.

# class ContactForm(forms.Form):
# 	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'contact-us__input-box', 'placeholder':'Kemisola'}))
# 	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'contact-us__input-box', 'placeholder':'Abdul'}))
# 	email_address = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'contact-us__input-box', 'placeholder':'abcd@wxyz.com'}))
# 	message = forms.CharField(widget=forms.Textarea(attrs={'class': 'contact-us__input-box', 'cols':'30', 'placeholder':'Hi, i would like to find out about ...'}))

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email_address', 'message',]

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'contact-us__input-box'})

	
class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

   

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
	
	
	class Meta:
		model = Profile
		fields = ['image']
 
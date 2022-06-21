from django.contrib.auth.models import User
from django import forms
from .models import Profile,NeighbourHood,Business,Post
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['profile_picture','bio','email','phone_no'] 
class HoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        fields=['name','location','description','image','health_center','health_email','health_contact']         
        
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields=['image','name','email','phone_no']            

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title','info'] 

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


        widgets = {
           'username' : forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}),
           'email' :forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email Address'}),
           'password1' : forms.TextInput(attrs={'class': 'form-control','placeholder':'password'}),
           'password2' :forms.TextInput(attrs={'class': 'form-control','placeholder':'Confirm Password'}),
    
        }      
       
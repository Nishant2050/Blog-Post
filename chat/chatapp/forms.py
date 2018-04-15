from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import VisitingPlaces, Post

class MyRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Required.Inform a valid email address')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class NewPlaceForm(forms.ModelForm):
    message = forms.CharField(max_length=4000, required=True, help_text='max length = 4000')

    class Meta:
        model = VisitingPlaces
        fields = ('place_name','location','message',)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('message',)


##    def save(self, commit=True):
##        user = super(UserCreationForm, self).save(commit=False)
##        user.first_name = self.cleaned_data['first_name']
##        user.last_name = self.cleaned_data['last_name']
##        user.email = self.cleaned_data['email']
##
##        if commit:
##            user.save()
##
##        return user
##    

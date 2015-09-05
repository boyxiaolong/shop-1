from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    country=forms.CharField(required=True)
    postal_code=forms.CharField(required=True)
    city=forms.CharField(required=True)
    address=forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2','country','postal_code','city','address')

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.country = self.cleaned_data['country']
        user.postal_code = self.cleaned_data['postal_code']
        user.city = self.cleaned_data['city']
        user.address = self.cleaned_data['address']

        if commit:
            user.save()

        return user
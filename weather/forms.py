from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import fields, widgets
from django.conf import settings
import requests

class SearchForm(forms.Form):
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))

    def search(self):
        result = {}
        city = self.cleaned_data['city']
        endpoint = 'http://dataservice.accuweather.com/locations/v1/cities/search?q={city_name}&apikey={api_key}'
        url = endpoint.format(city_name=city, api_key=settings.ACCUWEATHER_API_KEY)
        headers = {'q': city,'apikey': settings.ACCUWEATHER_API_KEY}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:  # SUCCESS
            result = response.json()
            print("result: ", result)
            result[0] = True
        else:
            result[1] = False
            if response.status_code == 404:  # NOT FOUND
                result['message'] = 'No entry found for "%s"'
            else:
                result['message'] = 'The API is not available at the moment. Please try again later.'
        return result

# SignUp Form
class SignupForm(UserCreationForm):
    # Changing fields structure 
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm'}))

    class Meta:
        model = User 
        fields = ['username','first_name', 'email']
        labels = {'email':'Email'}

# Login Form
class LoginForm(AuthenticationForm):
    # Changing fields structure 
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm'}))

    class Meta:
        model = User
        fields = ['username', 'password']

from django import forms
from .models import Account
from django.contrib.auth import authenticate

COUNTRY_CHOICES = [
    ('VN', 'Viet Nam'),
    ('US', 'United State'),
    ('HK', 'Hong Kong'),
]

CITY_CHOICES = [
    ('HCM', 'Ho Chi Minh'),
    ('BR-VT', 'Ba Ria-Vung Tau'),
    ('DN', 'Dong Nai'),
]
GENDER_CHOICES = [('M','Male'),('F','Female')]

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account        
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'sex',
            'phone_number',
            'city',
            'country',                   
        ]
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete':'off',                    
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete':'off',
                }
            ), 
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete':'off',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete':'off',
                }
            ),
            'phone_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete':'off',
                }
            ),
            'city': forms.Select(
                attrs={
                    'class': 'form-control',
                    'autocomplete':'off',                    
                }, choices=CITY_CHOICES,
            ),
            'country': forms.Select(
                attrs={
                    'class': 'form-control',
                    'autocomplete':'off',                    
                }, choices=COUNTRY_CHOICES,
            )
        }


class AccountAuthenticationForm(forms.ModelForm):

    #password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = [
            'email', 
            'password'
        ]

        widgets = {
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete':'off',                    
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete':'off',                    
                }
            ),
            }

    
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")


class AccountUpdateForm(forms.ModelForm):

	class Meta:
		model = Account
		fields = ('email', 'username', )

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
		except Account.DoesNotExist:
			return email
		raise forms.ValidationError('Email "%s" is already in use.' % account)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
		except Account.DoesNotExist:
			return username
		raise forms.ValidationError('Username "%s" is already in use.' % username)
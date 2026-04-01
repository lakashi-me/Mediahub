from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    user_type = forms.ChoiceField(choices=User.USER_TYPE_ROLES, 
                                  widget=forms.Select(attrs={'class': 'form-control'})) 
    class Meta:
        model = User
        fields = ['username', 'email', 'user_type', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        }
        def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
           self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Password'}))

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email','bio', 'profile_image' ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 
                                             'placeholder': 'Email'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 
                                         'rows': 3, 'placeholder': 'Bio'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
        }    
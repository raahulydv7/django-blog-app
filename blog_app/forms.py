from django import forms
from .models import UserProfile,Posts
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None  
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'autofocus': True}),
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
    )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['fname', 'lname', 'mob', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us about yourself...'}),
        }
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={
                'placeholder': 'Write something...',
                'rows': 4
            }),
        }

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs={
                'placeholder': 'Write something...',
                'rows': 4
            }),
        }
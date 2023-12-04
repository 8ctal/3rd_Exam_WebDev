from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['username'].help_text = ''
        del self.fields['password2']
    
    class Meta:
        model = User
        fields = ("email", "first_name", "username", "password1")
    
    # No sirvió
    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     print(f"validando {username}")
    #     if User.objects.filter(username=username).exists():
    #         raise forms.ValidationError('El nombre de usuario ya existe')
    #     return username

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

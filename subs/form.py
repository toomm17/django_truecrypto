from django.contrib.auth import get_user_model
from django import forms
from django.core.exceptions import ValidationError


User = get_user_model()


class LoginForm(forms.ModelForm):
    email = forms.EmailField(
        max_length=255, 
        widget=forms.EmailInput(attrs={'placeholder': 'TrueCrypto@gmail.com', 'class': 'modal-login__input'})
    )

    def clean(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise ValidationError(f'Пользователь не купил подписку.')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ('email', )

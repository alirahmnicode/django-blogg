from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        max_length=20,
        widget=forms.TextInput(attrs={"placeholder": "your username"})
    )
    password = forms.CharField(
        min_length=6,
        max_length=100,
        widget=forms.PasswordInput(attrs={"placeholder": "your password"})
    )


class UserRegisterForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        max_length=20,
        widget=forms.TextInput(
            attrs={"placeholder": "your username", "class": "username"})
    )

    email = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "your username"})
    )

    password1 = forms.CharField(
        min_length=6,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={"placeholder": "your password", "class": "password1"})
    )

    password2 = forms.CharField(
        min_length=6,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={"placeholder": "confirm your password", "class": "password2"})
    )

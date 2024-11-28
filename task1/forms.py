from django import forms

class UserRegisterForm(forms.Form):
    name = forms.CharField(max_length=30, label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Повторите пароль')
    age = forms.IntegerField(label='Возраст')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        age = cleaned_data.get("age")

        if password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают.")

        if age < 18:
            raise forms.ValidationError("Возраст должен быть не менее 18 лет.")
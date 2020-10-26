from django import forms
from django.contrib.auth.hashers import make_password, check_password
from .models import Dsuser

class RegisterForm(forms.Form):
    uid = forms.CharField(
        error_messages={
            'required' : '모든 값을 입력해야 합니다'
        },
        max_length=128, label='아이디'
    )

    email = forms.EmailField(
        error_messages={
            'required' : '모든 값을 입력해야 합니다'
        },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required' : '모든 값을 입력해야 합니다'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )
    re_password = forms.CharField(
        error_messages={
            'required' : '모든 값을 입력해야 합니다'
        },
        widget=forms.PasswordInput, label='비밀번호 확인'
    )

    def clean(self):
        cleaned_data = super().clean()
        uid = cleaned_data.get('uid')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password:
            if password != re_password:
                self.add_error('password', '비밀번호가 다릅니다')
                self.add_error('re_password', '비밀번호가 다릅니다')
            else:
                dsuser = Dsuser(
                    uid=uid,
                    email=email,
                    password=make_password(password)
                )
                dsuser.save()

class LoginForm(forms.Form):
    uid = forms.CharField(
        error_messages={'required' : '아이디를 입력하세요'},
        max_length=32,
        label="아이디")
    password = forms.CharField(
        error_messages={'required' : '비밀번호를 입력하세요'},
        widget=forms.PasswordInput,
        label="비밀번호")

    def clean(self):
        cleaned_data = super().clean()
        uid = cleaned_data.get('uid')
        password = cleaned_data.get('password')

        if uid and password:
            dsuser = Dsuser.objects.get(uid=uid)

            if not check_password(password, dsuser.password):
                self.add_error('password', '비밀번호를 틀렸습니다')
            else:
                self.uid = dsuser.uid
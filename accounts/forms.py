from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].help_text=None
        
        self.fields['username'].widget.attrs.update({'placeholder': '사용자 이름: 문자, 숫자 / 150자 이하'})
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'style': 'margin: 0 auto; width: 50%;'})
        self.fields['username'].label = 'username'
        self.fields['username'].label_suffix=''
        self.fields['password1'].widget.attrs.update({'placeholder': '비밀번호: 문자와 숫자 조합 / 최소 8자 이상'})        
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'style': 'margin: 0 auto; width: 50%;'})
        self.fields['password1'].label = 'password'
        self.fields['password1'].label_suffix=''
        self.fields['password2'].widget.attrs.update({'placeholder': '비밀번호 확인'})        
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})  
        self.fields['password2'].widget.attrs.update({'style': 'margin: 0 auto; width: 50%;'})
        self.fields['password2'].label = 'password confirm'
        self.fields['password2'].label_suffix=''

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({'placeholder': '사용자 이름'})
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'style': 'margin: 0 auto; width: 50%;'})
        self.fields['username'].label = 'username'
        self.fields['username'].label_suffix=''
        self.fields['password'].widget.attrs.update({'placeholder': '비밀번호'})        
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'style': 'margin: 0 auto; width: 50%;'})
        self.fields['password'].label = 'password'
        self.fields['password'].label_suffix=''

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
       
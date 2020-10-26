from django import forms
from .models import Post

class PostForm(forms.Form):
    image_url = forms.CharField(
        error_messages={
            'required' : '이미지 주소를 입력해주세요'
        }, max_length=1000, label='이미지 주소')
    contents = forms.CharField(
        error_messages={
            'required' : '내용을 입력해주세요'
        }, widget=forms.Textarea, label='내용')
    tags = forms.CharField(label='태그')
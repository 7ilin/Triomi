from django import forms

from decor.models import Call, Post


class CallForm(forms.ModelForm):

    class Meta:
        model = Call
        fields = ('name', 'phone_number', 'comment',)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
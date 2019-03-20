from django import forms

from decor.models import Call


class CallForm(forms.ModelForm):

    class Meta:
        model = Call
        fields = ('name', 'phone_number', 'comment',)

from django import forms
from .models import UserRequest, RequestMessage


class RequestForm(forms.ModelForm):
    class Meta:
        model = UserRequest
        fields = 'title', 'description', 'user'


class MessageForm(forms.ModelForm):
    class Meta:
        model = RequestMessage
        fields = 'text_message', 'user_request'

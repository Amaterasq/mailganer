from django import forms


class MailForm(forms.Form):
    subject = forms.CharField(
        max_length=100,
        label="Subject"
    )
    message = forms.CharField(
        max_length=500,
        label="Body"
    )
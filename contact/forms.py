from django import forms
from contact.models import ContactModel
from django.utils.translation import gettext_lazy as _


# class ContactForm(forms.Form):
#     name = forms.CharField(required=True, max_length=25)
#     email = forms.EmailField(required=True)
#     phone_number = forms.CharField(required=True, max_length=10)
#     message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('name', 'email', 'phone_number', 'subject', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter Message Here',
                                             'cols': 80, 'rows': 20}),
        }
        error_messages = {
            'name': {
                'max_length': _('This name is too long'),
            },
        }

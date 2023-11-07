from django import forms
from contact.models import ContactModel
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('name', 'email', 'phone_number', 'subject', 'message')
        labels = ({'name': 'Full Name',
                   'email': 'Email Address',
                   'phone_number': 'Phone Number',
                   'subject': 'Subject',
                   'message': 'Message'})

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full Name',
                                           'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email',
                                             'class': 'form-control'},),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number',
                                                   'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject',
                                              'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter Message Here',
                                             'cols': 80, 'rows': 20,
                                             'class': 'form-control'}),
        }

        error_messages = {
            'name': {
                'max_length': _('This name is too long'),
            },

        }

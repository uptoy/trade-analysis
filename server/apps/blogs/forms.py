from django import forms
from apps.blogs.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:

        model = Contact
        fields = ('name', 'email', 'message')

from django import forms
from blog.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:

        model = Contact
        fields = ('name', 'email', 'message')

from django import forms
from .models import Contact, NewsLetter

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'input', 'placeholder': 'Message'})
        }

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ('email', )
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Enter your email'})
        }

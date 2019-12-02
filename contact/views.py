from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm


def contact_page(request):
    forms = ContactForm()
    if request.method == 'POST':
        forms = ContactForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.add_message(request, messages.INFO, 'Submitted!')
            return redirect('contact')
    context = {
        'forms': forms
    }
    return render(request, 'contact/contact.html', context)

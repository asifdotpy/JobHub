from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from .models import Contact
from .forms import ContactForm


# Create your views here.
def index(request):
    return render(request, 'landing/index.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')

            contact = Contact(name=name, email=email,
                              subject=subject, message=message)
            contact.save()

            return render(request, 'contact.html', {'form': form, 'sent': True})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

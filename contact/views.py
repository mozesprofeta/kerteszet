from django.shortcuts import render
from .forms import ContactForm
from .models import Customer
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail

import datetime

# Create your views here.


def index(request):
    errors = []
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # if not request.POST.get('name', ''):
        #     errors.append('Enter a name.')
        # if not request.POST.get('email') and '@' not in request.POST['email']:
        #     errors.append('Enter a valid e-mail address.')
        # if not request.POST.get('text', ''):
        #     errors.append('Enter a message.')
        if form.is_valid():
            newcustomer = Customer(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                telephone=form.cleaned_data['telephone'],
                text=form.cleaned_data['text'],
                date=datetime.datetime.now(),
            )
            newcustomer.save()
            send_mail(
                'New customer',
                'Telephone number:'
                + str(form.cleaned_data['telephone'])
                + '\n'
                + form.cleaned_data['text'],
                form.cleaned_data['email'],
                ['mozesprofeta@gmx.com']
            )
            return HttpResponseRedirect(reverse('contact:index'))
    else:
        form = ContactForm()

    return render(
        request, 'contact/index.html',
        {'form': form}
    )

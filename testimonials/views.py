from django.shortcuts import render
from .models import Opinion
from random import randint
from django.template import RequestContext
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

import datetime

from .forms import TestimonialForm

# Create your views here.


# RANDOM_NUMBER = randint(1, Opinion.objects.count())


def index(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            newcustomer = Opinion(
                name=form.cleaned_data('name'),
                email=form.cleaned_data('email'),
                date=datetime.datetime.now()
            )
            newcustomer.save()
            return HttpResponseRedirect(reverse('testimonials'))
    else:
        form = TestimonialForm()
        return render(request, 'testimonials/index.html', {'form': form})

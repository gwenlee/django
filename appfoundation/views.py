#comment: 
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from .forms import PersonForm, ContactForm


#question: what is "request" object in Django? 
#answer: it is a HttpRequest object that contians data about the request (auto-created), so the response should also be HttpResponse object in Django.
def renderTest(request, name = 'Jess', year=2021, month='October'):
    return render(request, 'base.html', 
    {'name':name, 'year':year, 'month':month})

def Person_detail(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid (for security):
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # question: do you know what "form.cleaned_data" does?
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            email = form.cleaned_data['email']
            # category = form.cleaned_data['category']


            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'name.html', {'form': form})

def Subscribe(request):
 # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonForm(request.POST)
        # check whether it's valid (for security):
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # question: do you know what "form.cleaned_data" does?
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            category = form.cleaned_data['subscription']


            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PersonForm()

    return render(request, 'subscribe.html', {'form': form})





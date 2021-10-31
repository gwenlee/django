#comment: 
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

#question: what is "request" object in Django? 
#answer: it is a HttpRequest object that contians data about the request (auto-created), so the response should also be HttpResponse object in Django.
def renderTest(request, year=2021, month="October"):
    name = 'Jess'
    return render(request, 'base.html', 
    {'name':name, 'year':year, 'month':month})

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # question: do you know what "form.cleaned_data" does?
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'hello.html', {'form': form})



from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_fn(request):
    html = "<h1> Welcome to My Home Page </h1>"
    #return HttpResponse(html)

    return render(request, template_name='index.html')

def next_fn(request):
    html = "<h1> Welcome to My Next Page </h1>"
    return render(request, template_name='base/base.html')

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404

# Create your views here.
def index(request):
    return render(request, 'landing/index.html')


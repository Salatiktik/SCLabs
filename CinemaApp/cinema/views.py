import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'info':1}
    return render(request,'cinema/index.html',context)
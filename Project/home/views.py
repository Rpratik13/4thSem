from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("<b>Hello World</b>")
    return render(request,"navbar.html",{})
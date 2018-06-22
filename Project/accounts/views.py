from django.shortcuts import render
from django.http import HttpResponse

def index_accounts(request):
	return HttpResponse("you are at accounts home page")

# Create your views here.

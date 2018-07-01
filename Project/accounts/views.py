from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout

def index(request):
	return render(request, 'accounts/index.html')
# Create your views here.
def sign_up(request):
	if request.method=='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			#log in the user
			return redirect('index')
	else:
		form=UserCreationForm()

	return render(request, 'accounts/sign_up.html', {'form':form})

def log_in(request):
	if request.method == 'POST':
		form=AuthenticationForm(data=request.POST)
		if form.is_valid():
			user=form.get_user()
			login(request,user)
			return redirect('index')
			#log in the usercreationform
	else:
		form=AuthenticationForm()

	return render(request, 'accounts/log_in.html',{'form':form})

def log_out(request):
	if request.method == 'POST':
		logout(request)
		return redirect('index')
	else:
		return HttpResponse("log in first")

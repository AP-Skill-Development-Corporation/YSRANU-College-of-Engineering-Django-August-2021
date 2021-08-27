from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def register(request):
	form = RegistrationForm()
	if request.method=="POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("login")
		else:
			return HttpResponse("<h1>Invalid Data</h1>")
	return render(request,"register.html",{"form":form})


def signin(request):
	if request.method=="POST":
		username = request.POST["uname"]
		password = request.POST["pswd"]

		u = authenticate(username=username,password = password)
		if u:
			login(request,u)
			return redirect('home')
		else:
			return HttpResponse("Invalid Credentials!")
	return render(request,"login.html")


def signout(request):
	logout(request)
	return redirect("login")
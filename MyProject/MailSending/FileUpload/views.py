from django.shortcuts import render
from .forms import ProfileForm
from django.http import HttpResponse
from .models import Profile
# Create your views here.

def profile(req):
	form = ProfileForm()
	if req.method=="POST":
		form = ProfileForm(req.POST, req.FILES)
		if form.is_valid():
			form.save()
			return HttpResponse("Image Uploaded Successfully")
	return render(req,"profile.html",{'f':form})


def data(request):
	d = Profile.objects.all()
	return render(request,"data.html",{"data":d})
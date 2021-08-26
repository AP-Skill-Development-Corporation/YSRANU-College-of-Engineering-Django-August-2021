from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactUs

from django.core.mail import send_mail
from MailSending.settings import EMAIL_HOST_USER as from_mail
# Create your views here.


def home(request):
	return render(request,'home.html')
	
def contactUs(request):
	form = ContactUs()
	if request.method=="POST":
		form = ContactUs(request.POST)
		if form.is_valid():
			sub = form.cleaned_data['subject']
			body = form.cleaned_data['body']

			result = send_mail(sub,body,from_mail,['r.sireesha@apssdc.in'])

			if result:
				return HttpResponse("Mail Sent Successfully")
			else:
				return HttpResponse("Mail not sent")
	return render(request,'contact.html',{'form':form})

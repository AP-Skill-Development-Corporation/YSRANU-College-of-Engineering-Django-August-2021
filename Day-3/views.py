from django.shortcuts import render
from django.http import HttpResponse
from MyApp.models import Student

# Create your views here.

def sample(request):
	return HttpResponse("<h2>hai welcome to django workshop</h2>")

def home(request):
	return HttpResponse("<h4 style=background-color:skyblue;color:red;font-size:20px>hello guys how are you!</h4>")

def hello(request,name):
	return HttpResponse('My name is:{}'.format(name))

def hm(request,id):
	return HttpResponse('My roll number is:{}'.format(id))

def task(request,name,id):
	return HttpResponse('my name is:{} and my roll number is :{}'.format(name,id))

def basic(request):
	return render(request,'MyApp/basic.html')

def table(request):
	return render(request,'MyApp/table.html')

def inline(request):
	return render(request,'MyApp/inline.html')

def internal(request):
	return render(request,'MyApp/internal.html')

def external(request):
	return render(request,'MyApp/external.html')

def boot(request):
	return render(request,'MyApp/boot.html')

def offline(request):
	return render(request,'MyApp/offline.html')


def register(request):
	if request.method=="POST":
		na=request.POST['name']
		num=request.POST['rollnum']
		age=request.POST['age']
		mob=request.POST['mobile']
		em=request.POST['email']
		addr=request.POST['addr']
		Student.objects.create(name=na,rollnum=num,age=age,mobile=mob,email=em,address=addr)
		return HttpResponse("your data submitted successfully")
	return render(request,'MyApp/register.html')
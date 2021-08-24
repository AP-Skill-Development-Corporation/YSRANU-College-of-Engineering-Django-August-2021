from django.shortcuts import render,redirect
from django.http import HttpResponse
from MyApp.models import Student,Register
from MyApp.forms import Reg


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
		# return HttpResponse("your data is submitted successfully")
		return redirect('/details')
	return render(request,'MyApp/register.html')


def details(request):
	data=Student.objects.all()
	return render(request,'MyApp/details.html',{'data':data})

def update(request,id):
	data=Student.objects.get(id=id)
	if request.method=="POST":
		data.name=request.POST['name']
		data.rollnum=request.POST['rollnum']
		data.age=request.POST['age']
		data.mobile=request.POST['mobile']
		data.email=request.POST['email']
		data.address=request.POST['addr']
		data.save()
		return redirect('/details')
	
	return render(request,'MyApp/update.html',{'data':data})


def delete(request,id):
	ob=Student.objects.get(id=id)
	if request.method=="POST":
		ob.delete()
		return redirect('/details')
	return render(request,'MyApp/delete.html',{'info':ob})


def reg(request):
	if request.method=="POST":
		formdata=Reg(request.POST)
		if formdata.is_valid():
			formdata.save()
			return redirect('/display')
			
	formdata=Reg()
	return render(request,'MyApp/reg.html',{'data':formdata})


def display(request):
	data=Register.objects.all()
	return render(request,'MyApp/display.html',{'data':data})

def up(request,id):
	a=Register.objects.get(id=id)
	if request.method=="POST":
		u=Reg(request.POST,instance=a)
		if u.is_valid():
			u.save()
			return redirect('/display')
	u=Reg(instance=a)
	return render(request,'MyApp/up.html',{'u':u})

def de(request,id):
	d=Register.objects.get(id=id)
	if request.method=="POST":
		d.delete()
		return redirect('/display')
	return render(request,'MyApp/de.html',{'d':d})
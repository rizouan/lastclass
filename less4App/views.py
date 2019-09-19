from django.shortcuts import render, redirect
from .models import Employee,Department
from less4App.forms import EmployeeForm

from django.core.paginator import Paginator
from django.contrib import messages

from django.core.mail import send_mail
from django.core.mail import BadHeaderError
from django.conf import settings

from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from less4App.forms import ContactForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    emp = Employee.objects.all()

    context = {'title': 'Welcome', 'employees': emp}
    return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.error(request,'Insert successfully ')
                return redirect('/')
            except Exception as e:
                print("type error: " + str(e))
        else:
            pass
    else:
        form = EmployeeForm()
    return render(request,'create.html',{'form':form})

def edit(request, id):
        employee = Employee.objects.get(id=id)
        form = EmployeeForm(request.POST,request.FILES) #try
        # if request.method == "POST" and form.is_valid():
        #     form.cleaned_data['department'] = employee.department
        departments = Department.objects.all()
        return render(request,'edit.html', {'employee':employee,'departments': departments,'form':form})

def update(request, id):
        employee = Employee.objects.get(id=id)
        form = EmployeeForm(request.POST,request.FILES,instance=employee)
        if form.is_valid():
            try:
                form.save()
                return redirect('/emp/listemp')
            except Exception as e:
                print("type error: " + str(e))


        return render(request, 'edit.html', {'employee': employee})

def destroy(request, id):
	employee = Employee.objects.get(id=id)
	employee.delete()
	messages.error(request,'Delete successfully ')
	return redirect("/")

def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['to']
            message = form.cleaned_data['message']

            recipient_list = []
            recipient_list.append(from_email)
            try:
                 send_mail(subject, message, from_email, recipient_list)
                # email = EmailMessage(subject, message, to=recipient_list)
                # email.send()
            except BadHeaderError as e:
                print("Error: " + str(e))

            messages.error(request,'Email sent successfully ')
            return redirect('/')
    return render(request, "email.html", {'form': form})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            form.save()
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect("/")
    else:
        form = UserCreationForm(request.POST)

    context = {'form':form}
    return render(request,'registration/register1.html',context)
###################################################################################

def listdept(request):

        department = Department.objects.all()
        depatment_list = department
        paginator = Paginator(depatment_list, 5) # Show 5 contacts per page

        page = request.GET.get('page')
        departments = paginator.get_page(page)


        return render(request,"empapp/listDept.html",{'departments':departments})

def createdept(request):
        if request.method == "POST":
            form = DepartmentForm(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('/emp/listdept')
                except Exception as e:
                    print("type error: " + str(e))
        else:
            form = DepartmentForm()
        return render(request,'empapp/createDept.html',{'form':form})

def editDept(request, id):
        department = Department.objects.get(id=id)
        form = DepartmentForm(request.POST) #try

        return render(request,'empapp/editDept.html', {'department': department})

def updateDept(request, id):
        department = Department.objects.get(id=id)
        form = DepartmentForm(request.POST,request.FILES,instance=department)
        if form.is_valid():
            try:
                form.save()
                return redirect('/emp/listdept')
            except Exception as e:
                print("type error: " + str(e))


        return render(request, 'empapp/editDept.html', {'department': department})

def destroyDept(request, id):
        department = Department.objects.get(id=id)
        department.delete()
        return redirect('/emp/listdept')

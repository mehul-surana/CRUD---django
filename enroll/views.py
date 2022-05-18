from django.shortcuts import render,HttpResponseRedirect

# from crudproject.enroll.models import User
from .forms import StudentRegistration
from .models import User
# Create your views here.
# this function will add new items and show items 
def add_show(request):
    if request.method == 'POST':
        fm=StudentRegistration(request.POST)
        #one method to save data is
        # if fm.is_valid():
        #     fm.save()
        #another method to save data is
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            res=User(name=nm,email=em,password=pw)
            res.save()
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    stud=User.objects.all()
    return render(request, 'enroll/addandshow.html',{'form':fm,'stu':stud} )

# this function will delete
def delete_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
def update_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST ,instance=pi)
        if fm.is_valid():
            fm.save()
        fm=StudentRegistration()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)


    return render(request,'enroll/updatesstudent.html',{'form':fm})
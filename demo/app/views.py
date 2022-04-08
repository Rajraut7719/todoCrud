from django.shortcuts import render,HttpResponseRedirect

from .models import User
from .forms import StudentRegistration
# Create your views here.
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        

        if fm.is_valid():
            fm.save()
        fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    stud=User.objects.all()
    
    return render(request,'app/addandshow.html',{'stu':stud,'form':fm})


def delete_data(request,id):
    if request.method =='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update_data(request,id ):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        fm=StudentRegistration(instance=pi)
      
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request,'app/updatestudent.html',{'form':fm})
    
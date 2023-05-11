from django.shortcuts import render,HttpResponse,redirect
from CRUDapp.models import UserModel
from CRUDapp.forms import UserForm

# Create your views here.

def insert(request):
    if request.method =="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Record inserted successfully...!</h1>")

    else:
        form = UserForm()
    return render(request,'index.html',{'form':form})



def show(request):
    users = UserModel.objects.all()
    return render(request,'show.html',{'users':users})



def delete(request,id):
    user = UserModel.objects.get(id=id)
    user.delete()
    return redirect('/show')



def edit(request,id):
    user = UserModel.objects.get(id=id)
    return render(request,'edit.html',{'user':user})



def update(request,id):
    user = UserModel.objects.get(id=id)
    form = UserForm(request.POST,instance=user)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,'edit.html',{'user':user})




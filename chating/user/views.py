from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from user.models import User
from django.contrib import messages
from .form import userForm
from home.models import Rooms,Message
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.

def userLogin(request):
    page='Login'
    if request.method == "POST":
        email=request.POST.get('Email')
        password=request.POST.get('Password')

        # try:
        #     user=User.objects.get(email=email)
        # except:
        #     messages.error(request,'Email authentication failed')
        # try:
        #     user=User.objects.get(password=password)
        # except:
        #     messages.error(request,'password authentication failed')

        user=authenticate(request,email=email,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'Successfully logedin')
            return redirect('home')
        else:
            messages.error(request,'Incorrect Credentials...Please check again...')

    context={'page':page}
    return render(request,'login_register.html',context)

def userRegister(request):
    form=userForm()
    if request.method == "POST":
        form=userForm(request.POST,request.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.capitalize()
            user.save()
            login(request,user)
            messages.success(request,'successfully Registerd...')
            return redirect('home')
        else:
            messages.error(request,'Registration failed')
    context={'form':form}
    return render(request,'login_register.html',context)

@login_required(login_url='login')
def userLogout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request,'successfully logout')
        return redirect('home')
    return render(request,'logout.html')

@login_required(login_url='login')
def profile(request,pk):
    users=User.objects.get(id=pk)
    rooms=users.rooms_set.all()
    msgs=users.message_set.all()
    message=Message.objects.all()
    context={'users':users,'rooms':rooms,'msgs':msgs,'message':message}
    return render(request,'profile.html',context)

@login_required(login_url='login')
def updateProfile(request,pk):
    users=User.objects.get(id=pk)
    form=userForm(instance=users)
    if request.method == 'POST':
        form=userForm(request.POST,request.FILES, instance=users)
        if form.is_valid():
            form.save()
            login(request,users)
            messages.success(request,'Updated successfully')
            return redirect('profile',pk=users.id)
        else:
            messages.error(request,'something wrong happend')
    context={'form':form}
    return render(request,'updateprofile.html',context)

def chatUsers(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    users=User.objects.filter(
        Q(username__icontains=q)
    )
    context={'users':users}
    return render(request,'chat_users.html',context)
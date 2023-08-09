from django.shortcuts import render,redirect
from .forms import RoomForm
from django.contrib import messages
from .models import Rooms,Message,Doubt
from django.db.models import Q

from django.contrib.auth.decorators import login_required

def home(request):
    context={}
    return render(request,'home.html',context)

@login_required(login_url='login')
def createRoom(request):
    form=RoomForm()
    if request.method == 'POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            val=form.save(commit=False)
            val.user=request.user
            val.name=val.name.capitalize()
            val.password=request.POST.get('password')
            val.save()
            messages.success(request,'Successfully created')
            return redirect('available_rooms')
        else:
            messages.error(request,'something went wrong')

    context={'form':form}
    return render(request,'createroom.html',context)

@login_required(login_url='login')
def available_rooms(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    rooms=Rooms.objects.filter(
        Q(name__icontains=q)
    )
    context={'rooms':rooms}
    return render(request,'available_rooms.html',context)

@login_required(login_url='login')
def room(request,pk):
    rooms=Rooms.objects.get(id=pk)
    room_messages=rooms.message_set.all()
    if request.method =='POST':
        Message.objects.create(
            user=request.user,
            rooms=rooms,
            body=request.POST.get('body')
        )
        return redirect('room',pk=rooms.id)
    context={'rooms':rooms,'room_messages':room_messages}
    return render(request,'room.html',context)

@login_required(login_url='login')
def room_password(request,pk):
    rooms=Rooms.objects.get(id=pk)
    room=request.POST.get('password')
    if room == rooms.password or rooms.user == request.user:
        messages.success(request,'welcome')
        return redirect('room',pk=rooms.id)
    context={'rooms':rooms}
    return render(request,'room_password.html',context)

@login_required(login_url='login')
def updateRoom(request,pk):
    rooms=Rooms.objects.get(id=pk)
    form=RoomForm(instance=rooms)
    if request.method == 'POST':
        form=RoomForm(request.POST,instance=rooms)
        if form.is_valid():
            val=form.save(commit=False)
            val.name=val.name.capitalize()
            val.save()
            return redirect('room',pk=rooms.id)
    context={'rooms':rooms,'form':form}
    return render(request,'updateroom.html',context)

@login_required(login_url='login')
def deleteRoom(request,pk):
    rooms=Rooms.objects.get(id=pk)
    if request.method == 'POST':
        rooms.delete()
        messages.success(request,'Deleted')
        return redirect('available_rooms')
    context={'obj':rooms}
    return render(request,'delete.html',context)

@login_required(login_url='login')
def deleteMessage(request,pk):
    message=Message.objects.get(id=pk)
    if request.method == 'POST':
        message.delete()
        return redirect('room',pk=message.rooms.id)
    context={'obj':message.body}
    return render(request,'delete.html',context)

# doubts

def askDoubts(request):
    if request.method == 'POST':
        Doubt.objects.create(
            user=request.user,
            body=request.POST.get('body')
        )
        messages.success(request,'We got your complaint. we will update you with in 1 day.thank you for your time')
        return redirect('home')
    context={}
    return render(request,'ask.html',context)
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import Room, Message
# Create your views here.
from django.http import HttpResponse, JsonResponse


def home(request):
    return render(request, 'home.html')


def room(request, room):
    username = request.GET.get('username')  # getting from url like pk
    # suppose in room name someone enters coders in front end we get that data and store it in room_details
    room_details = Room.objects.get(name=room)
    # passing all variables to room.html
    return render(request, 'room.html', {'username': username, 'room': room, 'room_details': room_details})

 # function to send user to a chat room if it is already there else create a new one and send him there


def checkview(request):
    room = request.POST['room_name']  # getting room name
    username = request.POST['username']  # getting username
    if (Room.objects.filter(name=room).exists()):
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()  # whenever we create an object from models.py we need to say newobj.save()
        # weird syntax hard to understand
        return redirect('/'+room+'/?username='+username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(
        value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('message sent successfully')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    # filter messages from db acc to room
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})

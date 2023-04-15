from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, room):
    # getting the username
    username = request.GET.get('username')
    # getting the particular model which has the name of this room an example would be 'coders'
    room_details = Room.objects.get(name=room)

    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details,
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/' + room + '/?username=' +username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/' + room + '/?username=' +username)

def send(request):
    message = request.POST['message']  
    username = request.POST['username']  
    room_id = request.POST['room_id']  

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message send successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    # from the Message model, we are getting the messages from a room id.
    messages = Message.objects.filter(room=room_details.id)
    # returning JSON response a list of message values.
    return JsonResponse({"messages":list(messages.values())})


from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import models
from . import serializers


@csrf_exempt
def auth_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
                             
    if user:
        login(request,user)
        serializer = serializers.UserSerializer(user)
        return JsonResponse(serializer.data)
    return HttpResponse(status=401)

@csrf_exempt
def signup(request):
    if models.User.objects.filter(username=request.POST['username']).exists():
        return HttpResponse(status=403)
    else:
        u = models.User(username=request.POST['username'])
        u.set_password(request.POST['password'])
        u.save()
        login(request, u)
        serializer = serializers.UserSerializer(u)
        return JsonResponse(serializer.data)

def auth_logout(request):
    logout(request)
    return HttpResponse(status=200)
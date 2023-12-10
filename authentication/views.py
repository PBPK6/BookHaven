# Create your views here.
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Successful login status.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login successful!"
                # Add other data if you want to send data to Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login failed, account disabled."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login failed, check email or password again."
        }, status=401)

@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logged out successfully!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout failed."
        }, status=401)

@require_POST   
@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        form = UserCreationForm({"username": data['username'], "fullname": data['fullname'], "email": data['email'], "password1": data['password1'], "password2": data['password2']})
        if form.is_valid():
            form.save()
            return JsonResponse({
                "status": True,
                "message": "User successfully registered!"
            }, status=200)
        else:
            test = messages.get_messages(request)

            return JsonResponse({
                "status": False,
                "message": "Register failed!",
            }, status=401)
            
@login_required
@csrf_exempt
def update_username(request):
    if request.method == "POST":
        data = json.loads(request.body)
        new_username = data.get('new_username')

        if new_username:
            try:
                user = request.user
                user.username = new_username
                user.save()
                return JsonResponse({
                    "status": True,
                    "message": "Username updated successfully!"
                }, status=200)
            except Exception as e:
                return JsonResponse({
                    "status": False,
                    "message": f"Failed to update username. Error: {str(e)}"
                }, status=500)
        else:
            return JsonResponse({
                "status": False,
                "message": "Please provide a new username."
            }, status=400)
    else:
        return JsonResponse({
            "status": False,
            "message": "Invalid request method. Only POST allowed."
        }, status=405)
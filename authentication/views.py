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
from django import forms
from django.contrib.auth.decorators import login_required

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    fullname = forms.CharField(label = "Full")

    class Meta:
        model = User
        fields = ("username", "fullname", "email", 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None #"What should we call you, dear audience"
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        full_name = self.cleaned_data["fullname"].split()
        user.first_name = full_name[0]
        #print(user.first_name)
        user.last_name = full_name[-1]
        user.email = self.cleaned_data["email"]
        user.password = self.cleaned_data["password1"]
        user.set_password(user.password)
        user.save()
        #print(user.role)
        return user

@require_POST 
@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        form = RegisterForm({"username": data['username'], "fullname": data['fullname'], "email": data['email'], "password1": data['password1'], "password2": data['password2']})
        print(data['email'])
        print(data['fullname'])
        if form.is_valid():
            form.save()
            return JsonResponse({
                "status": True,
                "message": "User successfully registered!"
            }, status=200)
        else:
            print(form.errors.items())
            return JsonResponse({
                "status": False,
                "message": "Register failed!",
            }, status=401)
            
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
            
@login_required
@csrf_exempt
def update_username(request):
    if request.method == "POST":
        data = json.loads(request.body)
        new_username = data.get('new_username')
        new_email = data.get('new_email')
        new_fullname = data.get('new_fullname')
        first_name = new_fullname.split()
        new_firstname = first_name[0]
        print(type(new_fullname))
        print(new_fullname)

        if new_username:
            try:
                user = request.user
                user.username = new_username
                user.email = new_email
                user.first_name = new_firstname
                user.save()
                return JsonResponse({
                    "status": True,
                    "message": "Username updated successfully!"
                }, status=200)
            except Exception as e:
                print(e)
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
        
@csrf_exempt
def get_user_details(request):
    user = request.user
    if user.is_authenticated:
        username = user.username
        email = user.email
        first_name = user.first_name
        return JsonResponse({
            "username": username, 
            "email": email,
            "first_name": first_name,
        }, status=200)
    else:
        return JsonResponse({
            "error": "User not authenticated"
        }, status=401)
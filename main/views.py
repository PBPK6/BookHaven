from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.forms import BookForm
from main.models import Book
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from django.contrib import messages  
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
import csv, datetime



class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    fullname = forms.CharField(label = "Full")
    role = forms.ChoiceField(choices=(('R', 'Reader'), ('W', 'Writer')), required=True)

    class Meta:
        model = User
        fields = ("username", "fullname", "email", 'role', 'password1', 'password2')
        
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
        user.role = self.cleaned_data["role"] 
        user.save()
        #print(user.role)
        return user
    
    
    
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']  # Add other fields as needed
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
    

    
# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    user = request.user
    first_name = request.user.first_name
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A',
        #'last_login': request.COOKIES['last_login'],
        'user' : user,
        'firstname' : first_name,
    }

    return render(request, 'main.html', context)

def top(request):
    x = []
    with open('archive/Books.csv') as file:
        csv_reader = csv.DictReader(file)

        for line in csv_reader:
            x += [line['Book-Title']]
    context = {"Titles": x[:10]}
    return render(request, "top.html", context)

def library(request):
    titles = []
    images = []
    with open('archive/Books.csv') as file:
        csv_reader = csv.DictReader(file)

        for line in csv_reader:
            titles += [line['Book-Title']]
            images += [line['Image-URL-L']]
    context = {
        'titles' : titles[:100],
        'images' : images[:100],
    }
    return render(request, "library.html", context)

def booklist(request):
    user = request.user
    context = {
        'user' : user,
    }
    return render(request, "booklist.html", context)

def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            #sername = form.cleaned_data['username']
            #email = form.cleaned_data['email']
            #password = form.cleaned_data['password1']
            #role = form.cleaned_data['role']
            #first_name, middle_name, last_name = form.cleaned_data["fullname"].split()

            # Create the user with the selected role
            #user = User.objects.create_user(username=username, email=email, password=password, role=role, first_name=first_name, last_name=last_name)
            #user.role = role  # Assuming you have a UserProfile associated with User

            # Additional code to handle the user registration
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            response = HttpResponseRedirect(reverse("main:show_main")) 
            #response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = ProfileEditForm(instance=request.user)

    return render(request, 'edit.html', {'form': form})


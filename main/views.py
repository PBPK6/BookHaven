from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.forms import BookForm
from main.models import Book
import csv

# Create your views here.
def show_main(request):
    context = {
        'name': 'Pak Bepe',
        'class': 'PBP A'
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
    context = {}
    return render(request, "library.html", context)

def booklist(request):
    context = {}
    return render(request, "booklist.html", context)

def search_book(request):
    if request.method == "POST" and request.POST['Searched'] != '':
        Searched = request.POST['Searched']
        Books = Book.objects.filter(name__contains=Searched) # Filter books by name
        context = {
            'Searched': Searched,
            'Books': Books
        }
        return render(request, 'search_book.html', context)
    else:
        return HttpResponseRedirect(reverse('main:library'))
        
        # context = {
            
        # }
        # return render(request, 'search_book.html', context)
    
def create_book(request):
    form = BookForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_book.html", context)
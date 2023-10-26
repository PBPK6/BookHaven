from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('top/', top, name='top'),
    path('library/', library, name='library'),
    path('booklist/', booklist, name='booklist'),
    path('search_book', search_book, name='search_book'),
    path('create-book', create_book, name='create_book'),
]
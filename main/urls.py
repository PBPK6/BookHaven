from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('top/', top, name='top'),
    path('library/', library, name='library'),
    path('booklist/<str:username>', booklist, name='booklist'),
    path('search_book', search_book, name='search_book'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit/', edit_profile, name='edit'),
    path("api/books", get_books, name="get_books"),
    path('add_to_list/<int:id>', add_to_list, name="add_to_list"),
    path('delitem/<int:id>', delItem, name='delItem'),
    path('get_user_books/<str:username>', get_user_books, name='get_user_books'),
    path('addReview/', addReview, name='addReview'),
    path('getReviewsJson/', getReviewsJson, name='getReviewsJson'),
    path('reviews/', reviews, name='reviews'),
    path('json/', show_json, name='show_json'),
    path('create-flutter-review/', create_review_flutter, name='create_review_flutter'),
    path('edit-flutter-review/<int:id>', edit_review_flutter, name='edit_review_flutter'),
    path('delete-flutter-review/<int:id>', delete_review_flutter, name='delete_review_flutter'),
    path('get_user_books_flutter/', get_user_books_flutter, name="get_user_books_flutter"),
    path('add_to_list_fl/', add_to_list_fl, name="add_to_list_fl"),
    path('del_from_list_fl/', del_from_list_fl, name="del_from_list_fl"),
    path('del_from_library_fl/', del_from_library_fl, name="del_from_library_fl"),
    path('check_su/', is_superuser, name='is_superuser'),
    path('set_su/', set_superuser, name='set_superuser'),
    path('rem_su/', rem_superuser, name='rem_superuser'),
]
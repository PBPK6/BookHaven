from django.urls import path
from authentication.views import *

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('update_username/', update_username, name='update_username'),
    path('get_user_details/', get_user_details, name='get_user_details'),
]
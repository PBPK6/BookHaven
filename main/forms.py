from django.forms import ModelForm
from main.models import *

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["isbn", "title", "author", "year", "publisher", "image_s", "image_m", "image_l"]

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["book", "rate", "review", "user", "username"]
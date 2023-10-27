from django.forms import ModelForm
from main.models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["isbn", "title", "author", "year", "publisher", "image_s", "image_m", "image_l"]
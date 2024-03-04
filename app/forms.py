from django import forms

from .models import BooksModel,CategoriesModel


class BookForm(forms.ModelForm):
      class Meta:
            model = BooksModel
            fields = "__all__"

class CategoryForm(forms.ModelForm):
      class Meta:
            model = CategoriesModel
            fields = "__all__"
from django.contrib import admin
from .models import BooksModel,CategoriesModel
# Register your models here.
admin.site.register(BooksModel)
admin.site.register(CategoriesModel)
from django.shortcuts import render
from .models import BooksModel,CategoriesModel



def home(request):
      book = BooksModel.objects.all()
      return render(request,'app/home.html',{'home':home})
from django.shortcuts import render,redirect
from .models import BooksModel,CategoriesModel

from .forms import BookForm, CategoryForm

def home(request):
      book = BooksModel.objects.all()
      return render(request,'app/home.html',{'home':home})


def addCategory(request):
      if request.method == "POST":
            form = CategoryForm(request.POST)
            if form.is_valid():
                  form.save()
                  return redirect('home')
      form=CategoryForm()
      return render(request,'app/addCategory.html',{'form':form})
            
def addBook(request):
      if request.method == "POST":
            form = BookForm(request.POST)
            if form.is_valid():
                  form.save()
                  return redirect('home')
      form=BookForm()
      return render(request,'app/addBook.html',{'form':form})
            
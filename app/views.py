from django.shortcuts import render,redirect
from .models import BooksModel,CategoriesModel

from .forms import BookForm, CategoryForm

def home(request):
      books = BooksModel.objects.all()
      return render(request,'app/home.html',{'books':books})


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
            

def updateCategory(request,id):
      cat = CategoriesModel.objects.get(id=id)
      if request.method == "POST":
            form = CategoryForm(request.POST,instance=cat)
            if form.is_valid():
                  form.save()
                  return redirect('home')
      form=CategoryForm()
      return render(request,'app/updateCategory.html',{'form':form})
            
def updateBook(request,id):
      book = BooksModel.objects.get(id=id)
      if request.method == "POST":
            form = BookForm(request.POST,instance=book)
            if form.is_valid():
                  form.save()
                  return redirect('home')
      form=BookForm(instance=book)
      return render(request,'app/updateBook.html',{'form':form})
            
def deleteBook(request,id):
      book = BooksModel.objects.get(id=id)
      book.delete()
     
            
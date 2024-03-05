from django.shortcuts import render,redirect
from .models import BooksModel,CategoriesModel

from .forms import BookForm, CategoryForm
from .resource import BookResource
from tablib import Dataset
import pandas as pd
import os
from django.core.files.storage import FileSystemStorage



def Import_Excel_pandas(request):
     
    if request.method == 'POST' and request.FILES['myfile']:      
        myfile = request. FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)              
        empexceldata = pd.read_excel(filename)        
        dbframe = empexceldata
        for dbframe in dbframe.itertuples():
            obj = BooksModel.objects.create(
                  title = dbframe.title,
                  subtitle = dbframe.subtitle,
                  authors = dbframe.authors,
                  publisher = dbframe.publisher,
                  category= CategoriesModel.objects.filter(category=dbframe.category),
                  distribution_expense = dbframe.distribution_expense,   
             )           
            obj.save()
        return render(request, 'app/Import_excel.html', {
            'uploaded_file_url': uploaded_file_url
        })   
    return render(request, 'app/Import_excel.html',{})
 
 
def Import_Excel(request):
    
    if request.method == 'POST' and request.FILES['myfile']:      
        myfile = request. FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)    
        return render(request, 'app/Import_excel.html', {
            'uploaded_file_url': uploaded_file_url
        })   
    return render(request, 'app/Import_excel.html',{}) 

def Import_excel(request):
    if request.method == 'POST' :
        Employee =BookResource()
        dataset = Dataset()
        new_employee = request.FILES['myfile']
        data_import = dataset.load(new_employee.read())
        result = BookResource.import_data(dataset,dry_run=True)
        if not result.has_errors():
            BookResource.import_data(dataset,dry_run=False)        
    return render(request, 'app/Import_excel.html',{})

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
     
            
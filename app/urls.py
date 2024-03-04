from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    
    path('addCat',views.addCategory,name='addCat'),
    path('addBook',views.addBook,name='addBook'),
]

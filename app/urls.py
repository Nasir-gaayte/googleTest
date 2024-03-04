from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('import/',views.Import_Excel,name="import"),
    path('Import_excel',views.Import_excel,name="Import_excel"),
    path('Import_Excel_pandas/', views.Import_Excel_pandas,name="Import_Excel_pandas"),
    
    path('addCat',views.addCategory,name='addCat'),
    path('addBook',views.addBook,name='addBook'),
    path('updatebook/<id>/',views.updateBook,name='updateBook'),
    path('updateCat/<id>/',views.updateCategory,name='updateCat'),
    path('deleteBook/<id>/',views.deleteBook,name='deleteBook')
]

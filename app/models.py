from django.db import models



class CategoriesModel(models.Model):
      category=models.CharField(max_length=50)
      
      def __str__(self):
          return self.category

class BooksModel(models.Model):
      title = models.CharField(max_length=50)
      subtitle = models.CharField(max_length=150)
      authors = models.CharField(max_length=50)
      publisher = models.CharField(max_length=50)
      published_date = models.DateTimeField(auto_now_add=True)
      category =models.ForeignKey(CategoriesModel,on_delete= models.CASCADE)
      distribution_expense = models.FloatField()
      
      def __str__(self):
          return f"{self.title} by {self.authors}"
            
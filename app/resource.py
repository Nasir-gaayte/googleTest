from import_export import resources
from .models import BooksModel

class BookResource(resources.ModelResource):
      class Meta:
            model = BooksModel
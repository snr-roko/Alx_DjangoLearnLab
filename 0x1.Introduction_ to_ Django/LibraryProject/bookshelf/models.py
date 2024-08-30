from django.db import models

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length = 200)
  author = models.CharField(max_length = 100)
  publication_year = models.IntegerField()

  def __repr__(self):
    return f"Book(title='{self.title}', author='{self.author}', year={self.publication_year})"
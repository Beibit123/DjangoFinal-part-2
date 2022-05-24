from django.db import models


class BookJournalBase(models.Model):
    name = models.CharField("name", max_length = 50)
    description = models.CharField("description", max_length=300)
    price = models.FloatField("price")
    created_at = models.DateField("date")
       
    class Meta:
        abstract = True
        
class Book(BookJournalBase):
    num_pages = models.FloatField("num_pages")
    genre = models.CharField("genre", max_length=50)
    

class Journal(BookJournalBase):
    type = models.CharField("type", max_length=10)
    publisher = models.CharField("publisher", max_length=50)
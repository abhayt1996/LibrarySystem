from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    price = models.IntegerField()
    class Meta:
        db_table = "books"
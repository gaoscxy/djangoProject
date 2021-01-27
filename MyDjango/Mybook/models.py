from django.db import models

# Create your models here.

class Publisher(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=64,null=False,unique=True)

  def __str__(self):
    return "publisher_name:{}".format(self.name)

class Book(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=128,null=False)
  publisher = models.ForeignKey(to=Publisher,related_name="books",on_delete=models.CASCADE)

  def __str__(self):
    return "book_title:{}".format(self.title)

class Author(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=16,null=False)
  book = models.ManyToManyField(to="Book")

  def __str__(self):
    return "author_name:{}".format(self.name)
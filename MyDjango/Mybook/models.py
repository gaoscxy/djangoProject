from django.db import models

# Create your models here.

class Bookinfo(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=20)
    book_author = models.CharField(max_length=20)
    book_introduce = models.CharField(max_length=10000)
    book_update_time = models.CharField(max_length=20)
    order_no = models.IntegerField(default=0)

    def __str__(self):
      return self.book_name


class Chapterinfo(models.Model):
    chapter_id = models.AutoField(primary_key=True)
    chapter_name = models.CharField(max_length=200)
    chapter_path = models.CharField(max_length=500)
    bookinfo = models.ForeignKey(to=Bookinfo, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
      return self.chapter_name

class Versioninfo(models.Model):
    version_id = models.AutoField(primary_key=True)
    version_code = models.CharField(max_length=20)
    updatemsg = models.CharField(max_length=10000)

    def __str__(self):
      return self.version_code

    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

class Recommendinfo(models.Model):
    id = models.AutoField(primary_key=True)
    recommend_name = models.CharField(max_length=200)
    tel = models.CharField(max_length=20)

    def __str__(self):
      return self.version_code

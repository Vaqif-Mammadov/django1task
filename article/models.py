from django.db import models

# Create your models here.
class Article (models.Model):
    title=models.CharField(max_length=50, verbose_name="basliq")
    genre =models.CharField(max_length=35, verbose_name="janr")
    score=models.FloatField(verbose_name="bal")
    about=models.TextField(verbose_name="haqqinda")
    image=models.FileField(verbose_name="sekil")
    def __str__(self) :
        return self.title
    


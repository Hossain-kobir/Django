from django.db import models
from categories.models import Category
from author.models import Author
class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    Category = models.ManyToManyField(Category)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title}"
from django.db import models

class Article(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateField(auto_now=True)
    def snippet(self):
        return self.body[:50]+"..."
    

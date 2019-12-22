from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title   = models.CharField(max_length=120)
    date    = models.DateField(auto_now=True)
    content = models.TextField(blank=True)
    active  = models.BooleanField(default=True)
    
    # this method is used in article_list.html
    def get_absolute_url(self):
        return reverse('blog:article-detail', kwargs={'id':self.id})
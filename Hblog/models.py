from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields  import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('article_detail', args=(str(self.id)) )
        return reverse('home')



class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category =  models.CharField(max_length=255, default='coding')
    snippet =  RichTextField( blank=True, null=True )
    likes = models.ManyToManyField(User,blank=True, related_name='blog_posts')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')
    

    def total_likes(self):
        return self.likes.count()


    def __str__(self):  
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        # return reverse('article_detail', args=(str(self.id)) )
        return reverse('home')
        
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
    

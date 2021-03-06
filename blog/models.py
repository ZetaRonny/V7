import random
import os
from django.urls import reverse
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User


# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class PostManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) | 
                     Q(description__icontains=query)|
                     Q(slug__icontains=query)
                    )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookupsreturn qs
        return qs

def get_file_ext(filename):
    base_name = os.path.basename(filename)
    name , ext = os.path.splitext(filename)
    return name , ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_file_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "blogs/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename=final_filename)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, default="n/a")
    slug = models.SlugField(max_length=200, unique=True, default="n/a")
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to=upload_image_path,blank=True,null=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    objects = PostManager()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})
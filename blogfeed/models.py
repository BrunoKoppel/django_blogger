from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="the blogger")
    post_date = models.DateField(auto_now_add=True)
    header_image = models.ImageField(
        null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='uncategorized')
    likes = models.ManyToManyField(User, related_name='blog_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse("home")


class UserProfile(models.Model):
    meta_obj = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    # profile_picture = models.ImageField(null=True, )

    def __str__(self):
        return str(self.meta_obj)

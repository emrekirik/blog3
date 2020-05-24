from django.db import models
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = models.TextField()
    cover_image = models.ImageField(
        upload_to='post_image',
        blank=True,
        null=True,
    ) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return reverse('detail', kwargs={'id' : self.id})
   

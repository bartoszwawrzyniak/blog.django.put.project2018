from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
#rom PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #image = models.FileField(upload_to='post_image', blank=True)
    picture = models.FileField(blank=True, default="default.jpg", upload_to= 'media')
    #oldpicture = models.ImageField(default='new.jpg', upload_to = 'media') # image post
    #picture = models.ImageField(default="")
    #picture = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.title

    #def save(self): ##test
       # super().save()
 

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

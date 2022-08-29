from django.db import models
from api.models import User 
import datetime 

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    # image = models.ImageField(upload_to='image/post/'+ str(datetime.datetime.now()).replace(' ', '-') )
    # image = models.ImageField(upload_to='images')
    discription = models.CharField(max_length=500)
    post_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    comment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment[:10]



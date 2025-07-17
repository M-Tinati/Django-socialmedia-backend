from django.db import models
from django.contrib.auth.models import User
from accounts.models import  *
class Vote(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE , related_name="uvote")
    post = models.ForeignKey(Post,on_delete=models.CASCADE , related_name="pvote")
    
    def __str__(self):
        return f'{self.user}  like-> {self.post.slug}'

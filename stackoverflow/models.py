from django.db import models
from django.utils.text import Truncator
from django.utils.timezone import now
from django.contrib.auth.models import User
from forums.models import Forum
# Create your models here.


class Tag(models.Model): 
    
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=100)
    
# macro -> stackoverflow BYSTRO uppnut' - > models, serializers everywhere + test them on the Ps

# next macro -> new github deploy suka!!!  WITH THE NEW frontend!!! 

# 
class Question(models.Model): 

    parent_tag= models.ForeignKey(Tag, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)        
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()

class Answer(models.Model): 

    parent_question= models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question')
    created_at = models.DateTimeField(auto_now_add=True)        
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()





from rest_framework import serializers

from .models import Tag, Question, Answer









class TagSerializer(serializers.ModelSerializer): 

    class Meta: 
        model = Tag
        fields = [
            'name', 
            'description', 
            'id',
        ]

# 

# what the fuck are the serializers? ? ??

# ? ?? ?

class Question_Serializer(serializers.ModelSerializer): 

    class Meta: 
        model = Question
        fields = [
            'parent_tag', 
            'title', 
            'content', 
            'id', 
            'upvotes', 'downvotes'
        ]

    


class QAserializer(serializers.ModelSerializer): 
    parent_question = Question_Serializer(many = False)
    class Meta:  
        model = Question
        fields = [
            'parent_question', 
            'title', 
            'content', 
            'id', 
            'upvotes', 'downvotes'
        ]

# and the repetitions of those deicisions.
# 1. game of outputting data as a whole. 2. game of inputting data -> searching from the stash. 3. game of finding right serializer syntax
# 4. game of serializer as object or class structure wws. 5. game of views + testing 

# another macro game = github database + HEROKU database... 

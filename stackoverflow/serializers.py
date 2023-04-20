
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




class Question_Serializer(serializers.ModelSerializer): 

    class Meta: 
        model = Question
        fields = [
            'parent_tag', 
            'title', 
            'content', 
            'id', 
            'creator', 'created_at','upvotes', 'downvotes'
        ]

    


class Answer_serializer(serializers.ModelSerializer): 

    class Meta: 
        model = Question
        fields = [
            'parent_question', 
            'title', 
            'content', 
            'id', 
            'creator', 'created_at','upvotes', 'downvotes'
        ]
# 1 minutes decision -> limits of imitation of someone else's decisions. limit of my knowledge.
# everything in the future - will not be natural. 

# particularly = 2 shit options... 
# 

# here are to produce abstract algebra: different problems covering different shit -> to test the decisions they made
# and the repetitions of those deicisions.
# 1. game of outputting data as a whole. 2. game of inputting data -> searching from the stash. 3. game of finding right serializer syntax
# 4. game of serializer as object or class structure wws. 5. game of views + testing 

# another macro game = github database + HEROKU database... 
# 


class ParticularQuestionSerializer(serializers.Serializer): 
# Question + NEXT = answer to it!! 


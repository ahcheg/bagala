from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework .views import APIView
from rest_framework import status
from .models import Question, Answer, Tag

from rest_framework.exceptions import NotFound 
import datetime

from rest_framework.decorators import api_view
import json
from rest_framework import serializers
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import Question_Serializer, TagSerializer, QAserializer

from rest_framework.pagination import PageNumberPagination
from django.core.exceptions import ObjectDoesNotExist

# deployed, dal'we -> new game nahui. 1. what is outputted, 2. what is inputted and processed to database 3.
# here, stackoverflow -> every func nahuii. 
#  
# macro game -> is still -> api testing whatever. and frontend tuda-syuda + the interface of the frontend. 
# more abstract macro -> Stackoverflow + Auth + Nurate + Recommendations. 
# 


@api_view(['POST'])
def ask_question(request): 
    data = request.data
    serializer = Question_Serializer(data= data)
    """
            'parent_tag', 
            'title', 
            'content', 
            'id', 
         'upvotes', 'downvotes'
    """

    if(serializer.is_valid()): 
        serializer.save()
        return Response(serializer.data)
    else:
        raise NotFound()

@api_view(['GET'])
def get_hot_questions(request): 
    questions = Question.objects.all()
    serializer = Question_Serializer(questions, many= True)
    return Response(serializer.data)

    
@api_view(['GET'])
def get_recommendations(request): 
    questions = Question.objects.all()
    serializer = Question_Serializer(questions, many= True)
    return Response(serializer.data)


    
""" @api_view(['GET'])
def get_tags(request): 
    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many= True)

    return Response(serializer.data)


@api_view(['GET'])
def get_questions_by_tags(request): 
    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many= True)

    return Response(serializer.data)


    
@api_view(['GET'])
def get_question(request): 
    



    
@api_view(['POST'])
def upvote_question(request): 
    


    
@api_view(['POST'])
def downvote_question(request): 
    


    
@api_view(['POST'])
def add_answer(request): 
    


    
@api_view(['POST'])
def upvote_answer(request): 
    

    
@api_view(['POST'])
def downvote_answer(request): 
     """


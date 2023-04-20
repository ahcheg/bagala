from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework .views import APIView
from rest_framework import status
from .models import Courses, Files
from rest_framework.exceptions import NotFound 
import datetime

from rest_framework.decorators import api_view
import json
from rest_framework import serializers
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import CourseListSerializer, FileListSerializer, ToreSerializer

from rest_framework.pagination import PageNumberPagination
from django.core.exceptions import ObjectDoesNotExist


@api_view(['POST'])
def ask_question(request): 
    data = request.data
    
    
    course = Courses.objects.filter(id = course_ids).all().first()

    print(Courses.objects.get(id = 1))

    final_files = Files.objects.filter(parent_course= course, parent_course_category = category)
    if(final_files):
        serializer = FileListSerializer(final_files, many = True)



        return Response(serializer.data)
    else: 
        raise NotFound()
    
@api_view(['GET'])
def get_hot_questions(request): 
    return Response()

    
@api_view(['GET'])
def get_recommendations(request): 
    return Response()



    
@api_view(['GET'])
def get_tags(request): 
    return Response()


    
@api_view(['GET'])
def get_questionlist(request): 
    return Response()

    

    """
    path('askquestion/', include(), name = 'askquestion'), 
        path('hotquestions/',  include(), name = 'hotquestions'), 
    path('recommended/', include() , name = 'recommended_qs'), 
        path('question/<pk>', include() , name = 'precise_question'), 
        path('question/<pk>/answer', include(), name = 'answer_question'), 
        path('question/<pk>/upvote', include(), name = 'upvote_questionr'), 
        path('question/<pk>/answer/upvote', include(), name = 'upvote_answer'), 

    path('tags/',  include(), name = 'all_tags'), 
    path('tags/<pk>', include() , name = 'precise_tag'), 
        path('search/<slug>',  include(), name = 'search_question'), 
    """
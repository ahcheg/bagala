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


# new strat: fuck heroku and everything else... 
# first -> combine with bagala frontend... 
# 
# koroche -> stackoverflow + polnostyu obrabotat' each view and create a good databaase. 

# then -> combine 
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



    # fucking disappointment suka!! 
    # koroche now: 
    # stackoverflow full! 
    # losing: not doing any of these shit.
    # not reaching frontend -> losing is totally explainable
    # not reaching the backend stackoverflow -> losing is explainable
    # not reaching the pagination part NURATE and Questions!!! -> totally explainable. 
    # not reaching the whole combination of both -> also salamaleikum... 

    # the best strat would be -> immediately deploy to the frontend + establish the new game 

    # then the next quick strats would be -> devving stackoverflow and the rest in the new project ebat'. 

    # then the next quick strat would be -> sending the request by the buttons or whatever -> designing the interface,
    # then making requests and obtaining responses -> placing them somewhere.

    # best loss would be to mysticism. because banality - i don't want to lose in a banal way, just didn't reach the right lang. 
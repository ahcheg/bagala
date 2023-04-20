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



 # new quick plan: 
 # 1. home_page with files
 # 2. course_files_list 
 # 3. post_file 
 # 4. delete_file
 # 5. update_file 


 
@api_view(['GET'])
def home_everything(request, pk): 
    school_id = pk


    # SEDS 
    courses = Courses.objects.filter(parent_school = school_id)
    #print(seds.count())
   # ssh = Courses.objects.filter(parent_school = 2)
    #smg = Courses.objects.filter(parent_school = 3)
   # sme = Courses.objects.filter(parent_school = 4)
   # grad = Courses.objects.filter(parent_school = 5)


    course_serializer = CourseListSerializer(courses, many = True)
    #if course_serializer.is_valid():

   # print(course_serializer.data)
    #if (seds1.is_valid()):
  #  print(seds1.data)
  #  seds11 = ToreSerializer(data = {'school' : 'SEDS' , 'course_number': 1, 'courses': seds1})
   # if (seds11.is_valid()):
   #     print(seds11.data)
   # else:
    #    print(seds11.errors)     

   # ssh1 = CourseListSerializer(data = ssh)
   # ssh11 = ToreSerializer(data = {'SEDS', ssh.count(), ssh1})

    #smg1 = CourseListSerializer(data = smg)
   # smg11 = ToreSerializer(data = {'SEDS', smg.count(), smg1})

   # sme1 = CourseListSerializer(data = sme)
    #sme11 = ToreSerializer(data = {'SEDS', sme.count(), sme1})
#
    #grad1 = CourseListSerializer(data = grad)
    #grad11 = ToreSerializer(data = {'GRAD', grad.count(), grad1})


    #if seds11.is_valid() and ssh11.is_valid() and smg11.is_valid() and sme11.is_valid() and grad11.is_valid():
    #if course_serializer.is_valid():
    return Response(course_serializer.data)
    #else:
      #  return Response(status=status.HTTP_404_NOT_FOUND)



# quick decision 1 minute is needed: destroy.
# 1 min decision = someone's decision is json... 
# would be the smartest if i have recognized the course_id problem is mostly about testing other people's decisions. 
# 

# 1 mins for the macro decision - these decisions are so limited, and my further game is impossible. other's decisions involve tons of tests
# need to understand that. 
# 

@api_view(['GET'])
def course_file_list(request): 
    data = request.data
    print(data)
    course_ids = data['course_id']
    category = request.data['category']
    print(course_ids, category)
    course = Courses.objects.filter(id = course_ids).first()
    final_files = Files.objects.filter(parent_course= course, parent_course_category = category)
    if(final_files):
        serializer = FileListSerializer(final_files, many = True)



        return Response(serializer.data)
    else: 
        raise NotFound()
    
@api_view(['GET'])
def dynamically_get_course(request): 
    school_id = request.data.get('school_id')
    courses_list = Courses.objects.get(parent_school = school_id)
    courseserializer = CourseListSerializer(courses_list, many = True)
    return Response(courseserializer.data)

@api_view(['GET'])
def download_file(request): 
    file_id = request.get('file_id')
    file_to_return = Files.objects.get(id = file_id)
    file_serializer = FileListSerializer(file_to_return)
    return Response(file_serializer.data)


@api_view(['POST'])
def upload_file(request): 
    #school = request.data.get('school_id')
    #course_ids = request.data.get('course_id')
    #parent_course = Courses.objects.get(id = course_ids)
    #category = request.data.get('category')
    #file_name = request.data.get('file_name')
    #content = request.data.get('file_content')
    
    """
    parent_course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    #syllabus, assignments, quizzes/midterms, other materials
    parent_course_category = models.IntegerField(default = 0)
    name = models.CharField(max_length = 255)
    date_uploaded = models.DateField()
    content = models.FileField()

    """
    #files =  Files(parent_course = parent_course, parent_course_category = category, name = file_name, date_uploaded = datetime.datetime.now(), content = content)

    files =  FileListSerializer(data = request.data)

    if(files.is_valid()):


        files.save()
        return Response(files.data, status=status.HTTP_201_CREATED)    
    else: 
        print(files.errors)
        return Response(files.errors, status=status.HTTP_400_BAD_REQUEST)       

        

# nurate
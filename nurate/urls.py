from django.contrib import admin
from django.urls import path, include
from .views import home_everything, course_file_list, upload_file, dynamically_get_course,download_file, add_course
urlpatterns = [
    path('<int:pk>/', home_everything , name = "course_list"),
    path('files_list',course_file_list , name = "course_file_list"),
    path('upload_file',upload_file , name = "upload_file"),
    path('dynamic_courses', dynamically_get_course, name = "dynamic_courses"), 
    path('download_file', download_file, name = 'download_file'), 
    path('add_course',add_course, name='add_course' )


]


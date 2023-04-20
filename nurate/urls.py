from django.contrib import admin
from django.urls import path, include
from .views import home_everything, course_file_list, upload_file, dynamically_get_course,download_file
urlpatterns = [
    path('<int:pk>/', home_everything , name = "course_list"),
    path('files_list',course_file_list , name = "course_file_list"),
    path('upload_file',upload_file , name = "upload_file"),
    path('dynamic_courses', dynamically_get_course, name = "dynamic_courses"), 
    path('download_file', download_file, 'download_file')

    # to implement = search_file, search_course, PAGINATION!!!, Delete_file, update_file, upload Google Drive Link, upload only link to the file
    # 
    # 
]


# macro game -> a lot of decisions to be checked -> already kinda losing position... 
# stackoverflow wws -> a lot of stuff to be checked soo losing na tonen'kogo. 
# 
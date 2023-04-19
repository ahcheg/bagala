
from rest_framework import serializers

from .models import Courses, Files




"""
{
  school_name: string,
  course_number: string
  courses: [
    {
      course_name: string,
      course_desc: string
      course_id: string,
    }
  ]
}
"""

"""
 {
  label: string('syllabys for example'),
  files: []
}
"""




class CourseListSerializer(serializers.ModelSerializer): 

   # parent_course = serializers.CharField()
    class Meta: 
        model = Courses
        fields = [
            'name', 
            'description', 
            'id',
          #  'parent_course'
        ]

class ToreSerializer(serializers.Serializer): 
    school = serializers.CharField()
    course_number = serializers.CharField()
    courses  = CourseListSerializer(many = True)


class FileListSerializer(serializers.ModelSerializer): 

    class Meta: 
        model = Files
        fields = [
            'name', 
            'parent_course', 
            'parent_course_category', 
            'id', 
            'content', 'date_uploaded'
        ]



    

# losses = 1. Can ignore all the points to the postman
# 2. can lose getting partiuclar and testing my shit forever. 
# 3. 
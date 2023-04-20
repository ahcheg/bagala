
from rest_framework import serializers

from .models import Tag, Question, Answer




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

    
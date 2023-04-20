from django.db import models

# Create your models here.

    

class Courses(models.Model): 
    SCHOOL_CHOICES = (
    ("1", "SEDS"),
    ("2", "SSH"),
    ("3", "SMG"),
    ("4", "SME"),
    ("5", "Graduate"),
    )
    parent_school = models.CharField(max_length=32, choices=SCHOOL_CHOICES, default=1)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=100)
    


class Files(models.Model): 

    parent_course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    parent_course_category = models.IntegerField(default = 0)
    name = models.CharField(max_length = 255)
    date_uploaded = models.DateField()
    content = models.FileField(upload_to='staticfiles')
    
    class Meta: 
        ordering = [
            '-name'
        ]
    





from django.urls import include
from django.urls import path
from .views import ask_question


urlpatterns = [ 
    path('askquestion/', ask_question, name = 'askquestion'),


]
"""
urlpatterns = [ 
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
    
]
"""

from django.urls import include
from django.urls import path
from .views import


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
    # to implement search_question  + SEARCH questioN + RECOMMEND question + PROFILE AND HISTORY + MIGRATIONS !!! 
    # to_implement -> add the textbox that supports everything!!! 
    # 

    # impossible task1 : stable database everywhere -> 
#quick decision 1: 
    # 1. lost        
    # 2. heroku base dannih + frontend establishment + stackoverflow functions + parsing the data from registrar
    # evaluation of time 
    # - divide everything macro, - front + then stackoverflow + FRONT ITSELF DOING THE FRONT WWS -  AUTH - StackOverflow - FileAPI + Heroku.
    # next quick decision -> Heroku + FILE API + AUTH FIXING 
    # dividing Heroku -> Heroku needs data tables nahui. 
    # Heroku -> needs hz che. Heroku is big, can't destroy him, but I need more satisfaction from interacting from someone who is lying
    # Heroku = gets all from github, so it's ALLL up to github. 
    # if github is great, heroku is great too. then if github is great -> database -> can test from anywhere -> any test for the heroku: all the shitty fields. 
    # github is great, heroku is great -> mozhno spokoino zdes' base dannih + test it myself -> File + Auth. 
    # then deploy the front. then stackoverflow all the funcs dev from the zero!!! 
    # 


    # 2. AUTH + FRoNT + Stackoverflow this is the decision -> 
    # 3. parsing the data from reddit -> using this as primary... or whatever... accounts thougH? 
    # 4. all the mistakes division -> usually some type shit -> all the thing from outro -> returning precisely that and nothing else.
    # all of the restrictions and decisions made before do not affect me. what are the hidden steps and decisions -> i can make massive
    # micro or other people's decision mistakes(they are not natural) -> i can make mistakes in the imitation - no pohui. 
    # stackoverflow division -> abstract ->model-> serializers -> views -> urls -> again play this game twice or three times. 
    # view, serializers syntax or other people's decisions -> learn them. big decisions also exist here.
    # 
    # next losses = git commit + database + database filling + testing AUTH and Files + Heroku update. Failures and so on. 
    # 5. 

    # losses for the possible, creative losses: 1. database to github + the pushing up the database, pumping up 2. AUTH + FIle mistakes and requests.
    # 3. try to add search.  
    # how can i lose? all the creative ways. invent it yourself. can get stuck with functions and exploring, while main goal i 
    # s to get past through the gate fast. can get stuck studying here forever. 
    # I can creatively forget about the main goal.
    # pumping the database and testing - i can get stuck about what i need here actually
    # I might fail to understand and go back to play the math again and again. creatively refuse -> might see some chance and so on.
    # this shit is not easy and dissapointment actually. that's why.
    # already mostly lang, not math -> that's why i missed my moment of ingenuity. 
    # decision 1. pushing to github, via postman -> upload many files. then see heroku for update. check everything through postman
    # to heroku!!! 
    # 
    # new ways to lose: 
    # 1. not uploading the data. 
    # 2. not being able to understand and replay the game of the variable sampling. 
    # 3. not being able to repeat -> abstract data -> syntaxx and naoborot
    # 4. not being to understand scalability.
    #   can refuse -> it's a kind of loss -> because there were so many stupid system of assessments and their potential is still strong.
    #   can refuse -> coz didn't play macroest game... and didn't play how i can make micro mistake...
    # what is the central macro mistake here? not working directly with the given abstract math problems. 
    # speed is flashy, effective and might bring you money, fame and bithces, but usually useless and harmful for the research.
    # and also into the lang game without math again. you forgot about this loss too. 
    # you forgot to expect that mostly stuff -> razbirat' chuzhie der'mo resheniya and here a lot of creative ways to lose.
    # fuck speed, fuck wins, fuck every call. 

    # decision 1 -> create db -> the rest
]
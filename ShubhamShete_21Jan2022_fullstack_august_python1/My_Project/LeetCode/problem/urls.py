from django.urls import path
from problem import views

urlpatterns = [
    path('topic', views.create_topic),
    path('topic/<str:topic_id>', views.get_topic),
    path('difficulty', views.create_difficultylevel),
    path('difficulty/<str:diff_id>', views.get_difficultylevel),
    path('problem', views.create_problem),
    path('problem/<str:problem_id>', views.get_problem)
]

# {
#     "TopicID":1,
#     "TopicName":"React"
# }

# {
# "DiffID":1,
# "DiffLevel":"Easy"
# }

# {
#     "ProblemID":1,
#     "Author":1,
#     "TopicID":1,
#     "DiffID":1,
#     "Title":"React",
#     "Que":"What is React?",
#     "Ans":"It is a JavaScript library for building user interfaces."
# }

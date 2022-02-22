from django.urls import path
from User import views

urlpatterns = [
    path('user',views.user_create)
]

# {
#     "UserID": 1,
#     "FirstName": "Shubham",
#     "LastName": "Shete",
#     "Email": "shubham@gmail.com",
#     "Password": "s123"
# }

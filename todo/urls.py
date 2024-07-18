from django.urls import path
from .views import *

urlpatterns = [
    path("api/signup/", SignUp.as_view()),
    path("api/login/", Login.as_view()),
    path("api/todo/", CreateTodo.as_view(), name="todo-list-create"),
    path("api/todo/<int:pk>/", TodoAll.as_view()),
]

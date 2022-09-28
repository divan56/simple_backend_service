from django.urls import path, include
from .views import *

urlpatterns = [
    path('', StudentListOrCreateOne.as_view()),
    path('<int:id>/', StudentDetail.as_view()),
]

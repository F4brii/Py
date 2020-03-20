from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from schedule import views

urlpatterns = [
    path('schedule/', views.Teacher_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)
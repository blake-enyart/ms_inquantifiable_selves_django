from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from edamam_service import views

urlpatterns = [
    path('charts/', views.SnippetList.as_view()),
    path('charts/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

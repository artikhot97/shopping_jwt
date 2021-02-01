from django.conf.urls import url, include
from rest_framework import routers
from chapter_concept.views import ChapterAPIView

urlpatterns = [
    url(r'^chapter/', views.ChapterAPIView.as_view())
    url(r'^chapter/register/$', ChapterAPIView.as_view(), name='user-register'),
]
from django.contrib import admin
from django.urls import path,include
from student.views import studentviewset
from rest_framework import routers
from .views import SearchResultsView    

router= routers.DefaultRouter()
router.register(r'student',studentviewset)
 
urlpatterns = [
    path('',include(router.urls)),
    path('searchresults/',SearchResultsView.as_view(),name='SearchResults'), 
]   
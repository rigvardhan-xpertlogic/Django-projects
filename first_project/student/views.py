from django.shortcuts import render
from rest_framework import viewsets
from student.models import module_1         
from student.serializers import Sutdent_Serializer
from django.views.generic import ListView  

# Create your views here.
class studentviewset(viewsets.ModelViewSet):
    queryset=module_1.objects.all()
    serializer_class=Sutdent_Serializer

class SearchResultsView(ListView):   
    model =module_1                
    template_name = 'search_results.html' 

    def get_queryset(self):  
        query = self.request.GET.get("q")
        object_list = module_1.objects.filter(student_name__icontains=query)
        return object_list

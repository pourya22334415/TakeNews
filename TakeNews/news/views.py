from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import New



class NewsList(ListView):
    def get_queryset(self):
        return New.objects.all()
    
class NewsDetail(DetailView):
    def get_object(self):
        return get_object_or_404(
            New, 
            pk=self.kwargs.get("pk")
        )
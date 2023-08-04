from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import New

# Create your views here.
class NewsList(ListView):
    def get_queryset(self):
        return New.objects.all()
    
class NewsDetail(DetailView):
    def get_object(self):
        return get_object_or_404(
            New, 
            pk=self.kwargs.get("pk")
        )
from rest_framework.generics import ListCreateAPIView
from .serializers import NewsSerializer
from rest_framework import filters
from news.models import New

class NewsList(ListCreateAPIView):
    serializer_class = NewsSerializer
    queryset = New.objects.all()
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['tags']
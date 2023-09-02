from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from django.views.generic import ListView, DetailView
from .serializers import NewsDocumentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from django.http import HttpResponse
from .documents import NewsDocument
from elasticsearch_dsl import Q
from .models import New


class SearchNews(APIView, PageNumberPagination):
    news_serializer = NewsDocumentSerializer
    search_document = NewsDocument
    
    def get(self, request, query):
        try:
            q = Q(
                'multi_match', 
                query = query,
                fields = [
                    "content",
                ],
                fuzziness = 'auto',
            )
            
            search = self.search_document.search().extra(size = 10000).query(q)
            response = search.execute()
            
            results = self.paginate_queryset(response, request, view=self)
            serializer = self.news_serializer(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return HttpResponse(e, status=500)

class NewsList(ListView):
    def get_queryset(self):
        return New.objects.all().order_by("-id")

class NewsDetail(DetailView):
    def get_object(self):
        return get_object_or_404(
            New, 
            pk=self.kwargs.get("pk")
        )
        

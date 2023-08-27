from django.urls import path
from .views import NewsList, NewsDetail

app_name = "news"
urlpatterns = [
    path("", NewsList.as_view(), name="list"),
    path("<int:pk>", NewsDetail.as_view(), name="detail"),
]
from django.urls import path
from .views import NewsList, NewsDetail, SearchNews

app_name = "news"
urlpatterns = [
    path("", NewsList.as_view(), name="list"),
    path("<int:pk>", NewsDetail.as_view(), name="detail"),
    path("search/<str:query>/", SearchNews.as_view(), name="elasticsearch")
]
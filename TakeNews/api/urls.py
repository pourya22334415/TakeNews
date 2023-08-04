from django.urls import path
from .views import NewsList

app_name = "api"
urlpatterns = [
    path("", NewsList.as_view(), name="list")
]
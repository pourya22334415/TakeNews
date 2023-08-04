from rest_framework import serializers
from news.models import New

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'
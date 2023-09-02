from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .models import New
from .documents import NewsDocument

class NewsDocumentSerializer(DocumentSerializer):
    class Meta:
        model = New
        document = NewsDocument
        fields = '__all__'
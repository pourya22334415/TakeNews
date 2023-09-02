from django_elasticsearch_dsl.registries import registry
from django_elasticsearch_dsl import Document, fields   
from .models import New



@registry.register_document
class NewsDocument(Document):
    
    class Index:
        name = 'news'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }
        
    class Django:
        model = New 
        
        fields = ["id", "title", "content", "tags", "source"]

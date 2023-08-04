from .serializers import NewsSerializer
from django.test import TestCase
from news.models import New
        

class APITestCases(TestCase):
    def setUp(self):
        self.obj = {
            'title':'test_title',
            'content':'test_content',
            'tags':'test_tag',
            'sources':'test_source'
        }    

        self.expect_result = {
            'title': 'test_title',
            'content': 'test_content',
            'tags': 'test_tag',
            'sources': 'test_source'
        }
        
        self.new = New.objects.create(**self.obj)
        self.serializer = NewsSerializer(self.new)  
        
    def test_contains_expected_fields(self):
        data = self.serializer.data
        keys = ['id', 'title', 'content', 'tags', 'sources']
        self.assertEqual(set(data.keys()), set(keys))
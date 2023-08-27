from rest_framework.test import APITestCase
from rest_framework import status
from .models import New

class TakeNewsTestCases(APITestCase):
    def test_show_list_news(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_with_id(self):
        for new in New.objects.all():
            response = self.client.get("/%s", new.pk)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
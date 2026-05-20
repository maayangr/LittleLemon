from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        Menu.objects.create(title="Pizza", price=10, inventory=5)
        Menu.objects.create(title="Pasta", price=12, inventory=7)

    def test_getall(self):
        response = self.client.get('/menu-items/')
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
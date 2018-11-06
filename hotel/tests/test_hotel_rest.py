from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from hotel.models import Hotel, Company

class TestHotelRestFull(APITestCase):
    def setUp(self):

        self.company = Company.objects.create(name="Kenpisky", descripcion="Hotel description", code_id=1)
        self.hotel = Hotel.objects.create(company=self.company, name="Hotel Manzana", address="Manzana Gomez",
                                          city="La Habana", country="Cuba", telephone_number="")
        self.client = APIClient()
        self.uri = "http://localhost:8000/hotels/"


    def test_create_hotel(self):
        pass

    def test_list(self):
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))





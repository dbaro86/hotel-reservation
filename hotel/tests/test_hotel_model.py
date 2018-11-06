from django.test import  TestCase

from  hotel.models import Hotel

class HotelModelTest(TestCase):

    def test_string_representation(self):
        hotel = Hotel(name="Hotel Manzana", city="La Habana", country="Cuba" )
        self.assertEqual(str(hotel),hotel.name)
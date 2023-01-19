from datetime import datetime
from django.test import TestCase
from ..models import Booking, Menu
from django.utils.timezone import make_aware
from ..serializer import BookingSerializer, MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Ice Cream", price=3.50, inventory=120)
        Menu.objects.create(title="Orange Juice", price=5.00, inventory=200)
        Menu.objects.create(title="Green Tea", price=2.50, inventory=120)

    def test_getall(self):
        """Testing retrieving all of the created Menu records"""

        items = Menu.objects.all()
        serialized_items = MenuSerializer(items, many=True)

        self.assertEqual(len(serialized_items.data), 3)


class BookingViewTest(TestCase):
    def setUp(self):
        booking_date1 = make_aware(datetime.strptime("2023-01-17", "%Y-%m-%d"))
        booking_date2 = make_aware(datetime.strptime("2023-01-18", "%Y-%m-%d"))
        booking_date3 = make_aware(datetime.strptime("2023-01-19", "%Y-%m-%d"))
        booking_date4 = make_aware(datetime.strptime("2023-01-20", "%Y-%m-%d"))
        booking_date5 = make_aware(datetime.strptime("2023-01-23", "%Y-%m-%d"))

        Booking.objects.create(
            name="John Wick", no_of_guests=2, booking_date=booking_date1
        )
        Booking.objects.create(
            name="Fred Hamilton", no_of_guests=20, booking_date=booking_date2
        )
        Booking.objects.create(
            name="Cody Schmidt", no_of_guests=5, booking_date=booking_date3
        )
        Booking.objects.create(
            name="Brandon Lyons", no_of_guests=7, booking_date=booking_date4
        )
        Booking.objects.create(
            name="Annette Lorentz", no_of_guests=3, booking_date=booking_date5
        )

    def test_getall(self):
        """Test retriveing all of the created Booking records."""

        bookings = Booking.objects.all()
        serialized_items = BookingSerializer(bookings, many=True)

        self.assertEqual(len(serialized_items.data), 5)
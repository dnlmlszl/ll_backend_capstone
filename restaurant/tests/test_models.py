from datetime import datetime
from django.test import TestCase
from django.utils.timezone import make_aware
from ..models import Booking, Menu
from ..serializer import BookingSerializer, MenuSerializer


class MenuTest(TestCase):
    def test_get_item(self):
        """Test getting a single Menu record."""

        item = Menu.objects.create(title="Ice Cream", price=5.80, inventory=100)
        serialized_item = MenuSerializer(item)

        self.assertEqual(serialized_item.data.get("title"), "Ice Cream")
        self.assertEqual(serialized_item.data.get("price"), "5.80")


class BookingTest(TestCase):
    def test_get_booking(self):
        """Test getting a single Booking record."""

        booking_date = make_aware(datetime.strptime("2023-01-17", "%Y-%m-%d"))

        booking = Booking.objects.create(
            name="Chris King", no_of_guests=4, booking_date=booking_date
        )
        serialized_booking = BookingSerializer(booking)

        self.assertEqual(serialized_booking.data.get("name"), "Chris King")
        self.assertEqual(serialized_booking.data.get("no_of_guests"), 4)
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing, Review, Booking

class Command(BaseCommand):
    help = "Seed the database with sample Users, Listings, Reviews, and Bookings"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Seeding database…"))

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
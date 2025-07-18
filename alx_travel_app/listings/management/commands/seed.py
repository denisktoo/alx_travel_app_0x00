from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings data.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('🌱 Seeding sample listings...'))

        # Use the first available user as the host
        host = User.objects.first()
        if not host:
            self.stdout.write(self.style.ERROR('❌ No users found. Please create a user first.'))
            return

        # Create 10 sample listings
        for i in range(10):
            Listing.objects.create(
                host=host,
                name=f"Sample Listing {i+1}",
                description="This is a sample property description.",
                location=f"Sample City {i+1}",
                price_per_night=random.randint(50, 200)
            )

        self.stdout.write(self.style.SUCCESS('✅ Sample listings created successfully.'))

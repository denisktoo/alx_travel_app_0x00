from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listing
        fields = ['url', 'property_id', 'host', 'name', 'description', 'location', 'price_per_night', 'created_at', 'updated_at']

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ['url', 'booking_id', 'property', 'user', 'start_date', 'end_date' 'total_price', 'status', 'created_at']
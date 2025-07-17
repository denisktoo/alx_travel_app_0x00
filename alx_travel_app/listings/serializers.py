from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.HyperlinkedModelSerializer):
    host_name = serializers.SerializerMethodField()

    class Meta:
        model = Listing
        fields = ['url', 'property_id', 'host', 'host_name', 'name', 'description', 'location', 'price_per_night', 'created_at', 'updated_at']

    def get_host_name(self, obj):
        return f"{obj.host.first_name} {obj.host.last_name}"

class BookingSerializer(serializers.HyperlinkedModelSerializer):
    status = serializers.CharField()

    class Meta:
        model = Booking
        fields = ['url', 'booking_id', 'property', 'user', 'start_date', 'end_date', 'total_price', 'status', 'created_at']

    def validate_status(self, value):
        """
        Use serializers.ValidationError to validate status field.
        """
        allowed_statuses = ['confirmed', 'pending', 'cancelled']
        if value.lower() not in allowed_statuses:
            raise serializers.ValidationError(f"Status must be one of {allowed_statuses}.")
        return value
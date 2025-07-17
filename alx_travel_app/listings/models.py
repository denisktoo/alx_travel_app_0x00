from django.db import models
from django.contrib.auth.models import User

class Listing(models.Model):
    property_id = models.AutoField(primary_key=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Listing {self.property_id}: {self.name}"

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.review_id} by {self.user.first_name} for {self.property.name}"

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.booking_id} by {self.user.first_name} for {self.property.name}"

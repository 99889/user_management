
from django.db import models
from user_management.models import CustomUser  # Import the User model from the User Management microservice

class Auction(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_name = models.CharField(max_length=255)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Link the auction to the user who created it
    
    custom_field = models.CharField(max_length=255)
    

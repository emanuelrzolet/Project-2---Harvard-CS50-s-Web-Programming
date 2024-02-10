from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
class AuctionCategory(models.Model):
    title = models.CharField(max_length=64)

class Products(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=800)
    startingPrice = models.DecimalField(max_digits=100000, decimal_places=2)
    categories = models.ManyToManyField(AuctionCategory)
    imageUrl = models.TextField(default="empty")
    


class Bids(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    bid_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="bids")

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="comments")
    title = models.CharField(max_length=64)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
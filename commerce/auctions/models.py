from email.policy import default
from unicodedata import category
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
class AuctionCategory(models.Model):
    title = models.CharField(max_length=64)

#Create Listing: Users should be able to visit a page to create a new listing. They should be able to specify a title for the listing, a text-based description, and what the starting bid should be. Users should also optionally be able to provide a URL for an image for the listing and/or a category (e.g. Fashion, Toys, Electronics, Home, etc.).
class Products(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=800)
    startingPrice = models.DecimalField(max_digits=100000, decimal_places=2)
    categories = models.ManyToManyField(AuctionCategory)
    imageUrl = models.TextField(default="empty")
    
    
    pass


class Bids(models.Model):
    pass

class Comments:
    comment = Products()
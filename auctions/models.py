from enum import unique
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    Category = models.CharField(max_length=65)
    
    def __str__(self):
        return f"{self.Category} "


class Listing(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="lister")
    image = models.ImageField(upload_to='images')
    caption= models.CharField(max_length= 64,default="Image ofListing ")
    Item_Name = models.CharField(max_length=64)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="categories")
    Description = models.CharField(max_length=264)
    Starting_price = models.IntegerField()
    Highest_Bid = models.IntegerField(default=0)
    Auction_closed = models.BooleanField(default=False)

    def __str__(self):
        return f" Listing {self.pk}: {self.Item_Name} "

class Bid(models.Model):
    bidder_id = models.ForeignKey(User,on_delete=models.CASCADE, related_name="Bidder")
    item_id = models.ForeignKey(Listing,on_delete=models.CASCADE, related_name="listing")
    Bid_placed = models.IntegerField()

    def __str__(self):
        return f"${self.Bid_placed} bid placed by {self.bidder_id} on {self.item_id}"

class Comment(models.Model):
    item_id = models.ForeignKey(Listing,on_delete=models.CASCADE, related_name="Listing")
    Commenter_id = models.ForeignKey(User,on_delete=models.CASCADE, related_name="Commenter")
    Comment = models.CharField(max_length=264)
    
    def __str__(self):
        return f" Comment {self.pk} by {self.Commenter_id} on {self.item_id}"

class WatchList(models.Model):
    item_id = models.ForeignKey(Listing,on_delete=models.CASCADE, related_name="watchlist_item",unique=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="watchlist_owner")

    def __str__(self):
        return f"  {self.item_id.Item_Name} "




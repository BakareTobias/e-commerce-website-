from django.contrib import admin
from auctions.models import Bid, Category, Listing, User,Comment,WatchList

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(WatchList)


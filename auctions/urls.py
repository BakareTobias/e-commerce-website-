from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),#shop
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("closeAuction/<int:listing_id>",views.closeAuction,name="closeAuction"),
    path("createListing", views.createListing, name="createListing"),
    path("categories/<str:category_name>", views.categories, name="categories"),
    path("watchlist_add/<int:listing_id>", views.watchlist_add, name="watchlist_add"),
    path("watchlist_remove/<int:listing_id>", views.watchlist_remove, name="watchlist_remove"),
    path("profile/<int:id>", views.profile, name="profile"),
    path("listing/<int:listing>",views.listing_details, name="listing"),
    path("<str:listing>/bid",views.place_bid, name="PlaceBid"),
    path("<str:listing>/comment",views.leaveComment, name="leaveComment")
]

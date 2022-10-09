from cProfile import label
from email.mime import image
from logging import PlaceHolder
from tkinter.tix import DECREASING
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms

from .models import Bid, Category, Listing, User,Comment, WatchList


def index(request):
    return render(request, "auctions/index.html",{
        "listings":Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

class CommentForm(forms.Form):
        Leave_a_comment = forms.CharField(widget=forms.Textarea(attrs={'label':'g', 'style': 'width:905px; margin-bottom:20px;', 'class': 'form-control', 'height':'100px'}))


def listing_details(request,listing):
    list1ing= Listing.objects.get(pk=listing)
    try:
        top_bid =  Bid.objects.filter(item_id=listing).order_by('-Bid_placed').first().Bid_placed
        top_bid_owner =  Bid.objects.filter(item_id=listing).order_by('-Bid_placed').first().bidder_id
    except AttributeError:
        top_bid = list1ing.Starting_price
        top_bid_owner = ' '

    class BidForm(forms.Form):
        Bid = forms.IntegerField(label='Enter an amount',min_value=top_bid+1)
        WatchList = forms.BooleanField(label='Add to Watch List',required=False)
    
    try:
        comments =  Comment.objects.filter(item_id=listing).order_by('pk')
    except AttributeError:
        pass

    
    return render(request,"auctions/listing.html",{
        "listing":list1ing,
        "form":BidForm(),
        "topBid":top_bid,
        "topBidowner":top_bid_owner,
        "form2":CommentForm(),
        "comments":comments
})

def place_bid(request,listing,):
    if request.method == "POST":
        biD = Bid()
        biD.Bid_placed = request.POST["Bid"]
        biD.item_id = Listing.objects.get(pk=listing)
        biD.bidder_id = User.objects.get(id=request.user.id) 
        biD.save()
        try:
            print(request.POST["WatchList"])
            w = WatchList()
            w.item_id= Listing.objects.get(pk=listing)
            w.owner = User.objects.get(id=request.user.id) 
            w.save()
        except:
            print("off")
        
        return HttpResponseRedirect(reverse("listing",args=(listing,)))

def leaveComment(request,listing,):
    if request.method == "POST":
        comment = Comment()
        comment.item_id = Listing.objects.get(pk=listing)
        comment.Comment = request.POST["Leave_a_comment"]
        comment.Commenter_id = User.objects.get(id=request.user.id) 
        comment.save()

        return HttpResponseRedirect(reverse("listing",args=(listing,)))


def profile(request,id):
    user = User.objects.get(pk=id)
    listings= Listing.objects.filter(owner=user.id)
    bids = Bid.objects.filter(bidder_id=user.id)
    return render(request, "auctions/profile.html",{
        "bids":bids,
        "listings":listings,
        "buser":user
    })

def categories(request,category_name):#category here is the category name
    category_id = Category.objects.get(Category=category_name).pk#gets the name of the category
    listings = Listing.objects.filter(category=category_id)#listings with said categoryid
    all_cats = Category.objects.all()
    return render(request, "auctions/categories.html",{
        "listings":listings,
        "cat_name":category_name,
        "Categories":all_cats

    })


def watchlist(request):
    watchlist=WatchList.objects.filter(owner =request.user.id)
    return render(request, "auctions/watchlist.html",{
        "watchlist":watchlist
    })

TYPES = (  
    ('Sports', 'Sports', ),
    ('Other', 'Other', ),
    ('Phones and Accesories', 'Phones and Accesories', ),
    ('Furniture', 'Furniture', ), 
    ('Shoes','Shoes'),
    ('Clothes','Clothes') # Unlike other languages your last element can have a trailing comma too, its optional but still do that. I has some advantages which I am not gonna explain here
)

class ListingForm(forms.Form):
    Item_Name = forms.CharField(widget=forms.TextInput(attrs={ 'style': 'width: 300px; margin:20px;', }))
    Image= forms.ImageField()
    Alt_Text = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Description of your image', 'style': 'width: 300px; margin:20px;', }))
    Category = forms.MultipleChoiceField( choices=TYPES)
    Description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Short description of your listing', 'style': 'width: 300px; margin-bottom:20px;', }))
    Starting_Price = forms.IntegerField()



def createListing(request):
    if request.method == "POST":
        l = Listing()
        l.Item_Name = request.POST['Item_Name']
        l.owner =  User.objects.get(id=request.user.id) 
        l.image = request.POST["Image"]
        l.caption = request.POST['Alt_Text']
        l.category = Category.objects.get(Category= request.POST['Category'])
        l.Description = request.POST['Description']
        l.Starting_price = request.POST['Starting_Price']
        l.save()
    return render(request, "auctions/createListing.html",{
        "form":ListingForm()
    })
from django.contrib.auth.models import User, Group
from .models import Beer, Customer, Order, Review, Rating, Merch
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import BeerSerializer, CustomerSerializer, OrderSerializer, ReviewSerializer, RatingSerializer, MerchSerializer, UserSerializer, GroupSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]   

class BeerViewSet(viewsets.ModelViewSet):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer
    # permission_classes = [permissions.IsAuthenticated] 

class MerchViewSet(viewsets.ModelViewSet):
    queryset = Merch.objects.all()
    serializer_class = MerchSerializer
    permission_classes = [permissions.IsAuthenticated] 

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated] 

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated] 

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated] 

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated] 




from django.contrib.auth.models import User, Group
from .models import Customer, Beer, Order, Merch, Review, Rating
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer 
        fields = '__all__'


class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beer 
        fields = '__all__'
    
class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merch 
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review 
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating 
        fields = '__all__'
    

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order 
        fields = '__all__'
from django.db import models
from django.contrib.auth.models import User

SIZES = (
  ('S', 'Small'),
  ('M', 'Medium'),
  ('L', 'Large'),
   ('XL', 'Extra Large'),
  ('2XL', 'Doulbe Extra Large'),
)

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    phone_number = models.IntegerField()
    street_name = models.CharField(max_length=20)
    town = models.CharField(max_length=20)
    postcode = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return 'f{self.first_name} {surname}'    
    

class Beer(models.Model):
    title = models.CharField(max_length=50, unique=True)
    abv = models.FloatField(max_length=3)
    description = models.TextField()
    short_description = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.title 
    
class Merch(models.Model):
    title = models.CharField(max_length=50, unique = True)
    variant = models.CharField(max_length=50)
    size = models.CharField(
    max_length=3,
    choices=SIZES,
    default=SIZES[2][0]
  )
    description = models.TextField()
    short_description = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.title 


class Review(models.Model):
    title = models.CharField(max_length=50)
    review_content = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)


    def __str__(self):
        return self.title 


class Rating(models.Model):
    score = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)

    def __str__(self):
        return self.score  
    

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    beers = models.ManyToManyField(Beer)
    merch = models.ManyToManyField(Merch)
    
    def __str__(self):
        return self.id
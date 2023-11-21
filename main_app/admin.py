from django.contrib import admin
from .models import Beer, Merch, Order, Review, Rating, Image

# Register your models here.
admin.site.register(Beer)
admin.site.register(Merch)
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(Rating)
admin.site.register(Image)
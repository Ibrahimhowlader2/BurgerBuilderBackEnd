from django.contrib import admin
from BurgerApi.models import UserProfile,CustomarDetails,Order,Ingredient

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(CustomarDetails)
admin.site.register(Order)
admin.site.register(Ingredient)



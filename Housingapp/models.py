# from django.db import models
# from django.contrib.auth.models import User
# from phone_field import PhoneField
# from cloudinary.models import CloudinaryField

# #create models
# class Landlord(models.Model):
#     uname = models.TextField(max_length=100)
#     contact = PhoneField(null=True, blank=True)
#     email = models.EmailField(null=True, blank=True)
#     post = CloudinaryField('images', null=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE,null = True, related_name='user')
    
#     def __str__(self):
#         return f'{self.uname} Landlord'

# class Tenant(models.Model):
#     name = models.TextField(max_length=100)
#     contact = PhoneField(null=True, blank=True)
#     email = models.EmailField(null=True, blank=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE,null = True, related_name='user')
#     landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE,null = True, related_name='landlord')

#     def __str__(self):
#         return f'{self.name} Tenant'

# class Post(models.Model):
#      location = models.ForeignKey(Landlord, on_delete=models.CASCADE,null = True, related_name='landlord'))
#      category = models.ForeignKey(Landlord, on_delete=models.CASCADE,null = True, related_name='landlord')

# class Category(models.Model):
#     name=models.CharField(max_length=100)

# class Location(models.Model):
#     name=models.CharField(max_length=100)

from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    is_tenant = models.BooleanField(default=False)
    is_landlord = models.BooleanField(default=False)


class House(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='houses')
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0,blank=True, null=True)
    location = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    houses = models.ManyToManyField(House, through='ChosenHouse')
    


   
class Comment(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='tenant_comment')
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='house_chosen')
    text = models.TextField()


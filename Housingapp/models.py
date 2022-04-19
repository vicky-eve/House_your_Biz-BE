from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from cloudinary.models import CloudinaryField

#create models
class Landlord(models.Model):
    uname = models.TextField(max_length=100)
    contact = PhoneField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    post = CloudinaryField('images', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null = True, related_name='user')
    
    def __str__(self):
        return f'{self.uname} Landlord'

class Tenant(models.Model):
    name = models.TextField(max_length=100)
    contact = PhoneField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null = True, related_name='user')
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE,null = True, related_name='landlord')

    def __str__(self):
        return f'{self.name} Tenant'

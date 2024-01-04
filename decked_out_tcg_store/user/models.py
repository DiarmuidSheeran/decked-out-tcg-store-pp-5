from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static

class UserProfile(models.Model):
 
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200, null=True)
    lname = models.CharField(max_length=200, null=True)
    shipping_address_line_1 = models.CharField(max_length=255, null=True, blank=True)
    shipping_address_line_2 = models.CharField(max_length=255, null=True, blank=True)
    shipping_address_town = models.CharField(max_length=255, null=True, blank=True)
    shipping_address_county = models.CharField(max_length=20, null=True, blank=True)
    shipping_address_eircode = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.fname} {self.lname}"

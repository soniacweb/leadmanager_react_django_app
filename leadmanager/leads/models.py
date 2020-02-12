from django.db import models

# Create your models here.

# we want to pass in models.Mode so we can use some of the objects from the core model class
# then i defined the fields i wanted, name
#charfield is simply text 
#emailfield validates an email address, and setting emails to unique  
#also wanred message ot be optional so added in blank=true
# created_at includes a date time field adds date automatically

class Lead(models.Model):
  name = models.CharField(max_length=100)
  name = models.EmailField(max_length=100, unique=True)
  message = models.CharField(max_length=500, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
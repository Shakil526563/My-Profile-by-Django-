from django.db import models

# Create your models here.
class contact(models.Model):
    Name =models.CharField(max_length=20)
    Email_Address =models.EmailField(max_length=20)
    Text =models.CharField(max_length=20)
    
def __str__(self):
 return self.Name
from django.db import models
from shortuuid.django_fields import ShortUUIDField
# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    flag = models.FileField(upload_to="category",default="category.jpg",null=True,blank=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural="Countries"
        ordering = ["name"]
        
class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    active = models.BooleanField(default=True)
    sid = ShortUUIDField(
        length=10,
        alphabet="abcdefg1234",
        unique=True,)

    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name_plural="States"
        ordering = ["name"]
        

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    active = models.BooleanField(default=True)
    cid = ShortUUIDField(
        length=10,
        alphabet="abcdefg1234",
        unique=True,)

    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name_plural="Town / City"
        ordering = ["name"]
        

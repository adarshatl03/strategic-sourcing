from django.db import models
# from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.models import AbstractUser
import shortuuid
from shortuuid.django_fields import ShortUUIDField
# Create your models here.
shortuuid.set_alphabet("abcdefghijk")

class User(AbstractUser):
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=100,null=True,blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    # groups = models.ManyToManyField(
    #     Group,
    #     related_name='userauths_user_set',  # Custom related_name
    #     blank=True
    # )

    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     related_name='userauths_user_permissions',  # Custom related_name
    #     blank=True
    # )

    def __str__(self):
        return self.email
    
    def save(self,*args,**kwargs):
        email_username, mobile = self.email.split("@")

        if self.full_name == "" or self.full_name == None:
            self.first_name == email_username

        if self.username == "" or self.username == None:
            self.username == email_username

        super(User, self).save(*args, **kwargs)


class Profile(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.FileField(upload_to="image",default="default/default-user.jpg",null=True,blank=True)
    full_name = models.CharField(max_length=100,null=True,blank=True)
    about = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=100,null=True,blank=True)
    country = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    pid = ShortUUIDField(unique=True,length=10,max_length=20)

    def __str__(self):
        if self.full_name:
            return str(self.full_name)
        else:
            return str(self.user.full_name)
        
    def save(self,*args,**kwargs):
       

        if self.full_name == "" or self.full_name == None:
            self.full_name == self.user.full_name


        super(Profile, self).save(*args, **kwargs)

    




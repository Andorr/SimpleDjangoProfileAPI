from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
# Do I create my models here?

class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""

    def create_user(self, email, name, password=None):
        """Creates a new user profile object."""

        """Was a email provided?"""
        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new superuse with given details."""

        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        
        user.save(using=self._db)

        return user
        
        

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a "user" profile inside our system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get a users full name"""

        return self.name

    def get_short_name(self):
        """Used to get a users short name"""

        return self.name

    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""

        return self.email

class ProfileFeedItem(models.Model):
    """Profile status update"""

    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Django uses this to convert the FeedItem to a string"""

        return self.status_text

class ProfileMessage(models.Model):
    """A message to another profile"""

    to_profile = models.ForeignKey(UserProfile, related_name="receiver_profile", on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, related_name="user_profile", on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """The ProfileMessage as a string"""

        return "From: {} , To: {} , Message: {}".format(self.user_profile, self.to_profile, self.message)

class Post(models.Model):
    """A Post created by profiles"""

    poster = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.CharField(max_length=510)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """The post in form of a string"""

        return "Posted by: {} at {}, Text: {}".format(self.poster, self.text, self.time)





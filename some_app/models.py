from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class UserManager(BaseUserManager):
  '''
  creating a manager for a custom user model
  https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#writing-a-manager-for-a-custom-user-model
  https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#a-full-example
  '''
  def create_user(self, email, password=None):
    """
    Create and return a `User` with an email, username and password.
    """
    if not email:
      raise ValueError('Users Must Have an email address')

    user = self.model(
      email=self.normalize_email(email),
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

def create_superuser(self, email, password):
  """
  Create and return a `User` with superuser (admin) permissions.
  """
  if password is None:
    raise TypeError('Superusers must have a password.')

  user = self.create_user(email, password)
  user.is_superuser = True
  user.is_staff = True
  user.save()

  return user

class User(AbstractBaseUser):
  # username = models.CharField(max_length=255, unique=True, null=False)
  email = models.EmailField(max_length=255, unique=True)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['password']

  objects = UserManager()

  def __str__(self):
    return self.email
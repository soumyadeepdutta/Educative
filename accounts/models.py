from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
# from django.utils import timezone


class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def _create_user(self, email, password, first_name, last_name, **other):
        """
        Create and save user with given first name, last name and email
        """
        if not (email or password or first_name or last_name):
            raise ValueError('Email, Password, First Name and Last Name are required field!!')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **other)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email=None, first_name=None, last_name=None, password=None, **other):
        other.setdefault('is_superuser', False)
        other.setdefault('is_staff', False)


    def create_superuser(self, email=None, password=None, first_name=None, last_name=None, **other):
        """
        Create a superuser
        give some default permissions
        """

        other.setdefault('is_superuser', True)
        other.setdefault('is_staff', True)
        
        if other.get('is_superuser') is not True:
            raise ValueError('Superuser must be is_superuser')
        elif other.get('is_staff') is not True:
            raise ValueError('Superuser must be is_staff')

        
        return self._create_user(email, password, first_name, last_name, **other)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Django custom user model
    AbstructBaseUser: Defines the properties required for user mode;
    PermissionMixin: Have some methods to check or set permissions
    """

    email = models.EmailField(_('email'), max_length=128, unique=True, error_messages= {
        'unique': _("A user with that username already exists."),
    })
    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=80)

    date_joined = models.DateTimeField(auto_now_add=True)

    # teacher can post courses
    is_teacher = models.BooleanField(_('user is teacher'), default=False)

    # staff user can access adminpanel
    is_staff = models.BooleanField(_('is staff'), help_text='Can access admin panel', default=False)
    is_active = models.BooleanField(_('user is active'), default=True, help_text='Don\'t delete user, set False')

    # password and last_login is defined in AbstructBaseUser

    REQUIRED_FIELDS = ['first_name', 'last_name']

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email
    
    @property
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
    

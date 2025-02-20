from django.apps import apps
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.contenttypes.models import ContentType
from django.db.models import PositiveSmallIntegerField, TextChoices, CharField, EmailField, Model, SmallIntegerField, \
    ImageField, ForeignKey, CASCADE, FileField


class CustomUserManager(UserManager):
    def _create_user(self,  email, password, **extra_fields):

        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)


        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,  email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user( email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user( email, password, **extra_fields)


class User(AbstractUser):
    class UserRole(TextChoices):
        ADMIN = 'admin' , "Admin"
        USER = 'user' , "User"
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    username = None
    email = EmailField("Email address", blank=True, unique=True)
    objects = CustomUserManager()
    rank = PositiveSmallIntegerField(default=0)
    role = CharField(max_length=50, choices=UserRole.choices, default=UserRole.USER)


class Book(Model):
    name = CharField(max_length=255)
    level = SmallIntegerField()
    image = ImageField(upload_to="books/")


class Unit(Model):
    unit_num = SmallIntegerField(default=1)
    book = ForeignKey('apps.Book' , CASCADE , related_name='units')

class Vocab(Model):
    en = CharField(max_length=255)
    uz = CharField(max_length=255)
    audio_file = FileField(upload_to='vocab/audio/')
    unit = ForeignKey("apps.Unit", CASCADE, related_name='vocabs')


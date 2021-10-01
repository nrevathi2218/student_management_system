from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from student_managemnet_app.models import CustomUser


class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser,UserModel)

'''class UserModel(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []'''

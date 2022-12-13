import uuid
from django.conf import settings
from django.db import models
# from django.contrib.auth.models import AbstractUser
# from . user import CustomUserManager

# Create your models here.

# Custom user models
# class CustomUser(AbstractUser):
#     username = None
#     first_name = models.CharField(max_length=250)
#     last_name = models.CharField(max_length=250)
#     email = models.EmailField(max_length=100, unique=True)
#     phone_number = models.CharField(max_length=11)
#     isParent = models.BooleanField(default=False)
#     isSchool = models.BooleanField(default=False)

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ['first_name', 'last_name']

#     object = CustomUserManager()

#     class Meta:
#         ordering = ["-email"]
#         verbose_name = 'User'

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

class School(models.Model):
    # school = models.OneToOneField(settings.AUTH_USER_MODEL, limit_choices_to={'isSchool': True}, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    state = models.CharField(max_length=50)
    LGA = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    website = models.CharField(max_length=100, blank=True, null=True)
    unique_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    reg_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    first_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    middle_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=6)
    student_class = models.CharField(max_length=15)
    nationality = models.CharField(max_length=20)
    state = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    school = models.OneToOneField(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

class Sponsor(models.Model):
    # parent = models.OneToOneField(settings.AUTH_USER_MODEL, limit_choices_to={'isParent': True}, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    relationship = models.CharField(max_length=10)
    gender = models.CharField(max_length=6)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=11)
    state = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    NIN = models.CharField(max_length=50)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

class Debtor(models.Model):
    posted_by = models.ForeignKey(School, on_delete=models.CASCADE)
    # parent_details = models.ForeignKey(settings.AUTH_USER_MODEL, limit_choices_to={'isParent': True}, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    academic_session = models.DateField()
    status = models.CharField(max_length=5)
    amount = models.FloatField()
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)

    def str(self):
        return self.first_name


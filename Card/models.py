from django.db import models


# Create your models here.
class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    birth_date = models.DateField()
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=15, null=True)
    job_field = models.CharField(max_length=30)
    address = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='')

    # Communicated Link
    github = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    telegram = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

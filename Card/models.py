import os
from glob import glob
from pathlib import Path

from PIL import Image
from django.db import models


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

    def delete_older_profile_pic(self):
        parent_path = Path(self.profile_pic.path).parent
        images = glob("{}/*.png".format(parent_path))
        images.extend(glob("{}/*.jpg".format(parent_path)))

        for image in images:
            os.remove(image)

    def save(self, *args, **kwargs):
        super(PersonalInfo, self).save(*args, **kwargs)

        if self.profile_pic:
            with Image.open(self.profile_pic.path) as img:
                image = img.resize((200, 200))

                self.delete_older_profile_pic()
                image.save(self.profile_pic.path, quality=90)

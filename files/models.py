from django.db import models


class Image(models.Model):
    image = models.ImageField("Image", upload_to="uploads")

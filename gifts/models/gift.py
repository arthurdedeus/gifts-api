from django.db import models

from base_model import BaseModel


class Gift(BaseModel):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.IntegerField(help_text="Price in cents")
    amount = models.IntegerField(help_text="Amount available")
    image = models.ImageField(upload_to="gifts/images/")

    def __str__(self):
        return self.name

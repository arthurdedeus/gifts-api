from django.db import models


class Gift(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.IntegerField(help_text="Price in cents")
    amount = models.IntegerField(help_text="Amount available")
    image = models.ImageField(upload_to="gifts/images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

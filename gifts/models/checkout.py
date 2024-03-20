from django.conf import settings
from django.db import models

from base_model import BaseModel


class Checkout(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    qr_code = models.ImageField(
        upload_to="purchases/qr_codes/",
        help_text="QR Code for Pix payment",
    )

    @property
    def total(self):
        return self.checkout_items.aggregate(total=models.Sum("total"))["total"]

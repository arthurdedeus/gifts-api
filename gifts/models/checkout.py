from io import BytesIO

from django.conf import settings
from django.core.files import File
from django.db import models

from base_model import BaseModel
from gifts.services.pix import PixService


class Checkout(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(
        help_text="Message written by the gifter",
        blank=True,
        null=True,
    )
    qr_code = models.ImageField(
        upload_to="purchases/qr_codes/",
        help_text="QR Code for Pix payment",
    )
    br_code = models.CharField(
        max_length=1024,
        help_text="BR Code for Pix payment",
    )

    @property
    def total(self):
        return self.checkout_items.aggregate(total=models.Sum("total"))["total"]

    def generate_qr_code(self):
        pix_service = PixService()
        qr_code = pix_service.create_qr_code(amount=self.total)
        if qr_code:
            blob = BytesIO()
            qr_code.save(blob, format="PNG")
            self.br_code = pix_service.get_br_code()
            self.qr_code.save(f"qr_code_{self.id}.png", File(blob))

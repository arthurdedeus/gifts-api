from django.db import models

from base_model import BaseModel


class CheckoutItem(BaseModel):
    checkout = models.ForeignKey(
        "Checkout",
        on_delete=models.DO_NOTHING,
        related_name="checkout_items",
    )
    gift = models.ForeignKey("Gift", on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1)
    total = models.IntegerField()

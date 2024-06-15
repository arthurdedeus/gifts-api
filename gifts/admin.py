from django.contrib import admin

from gifts.models.checkout import Checkout
from gifts.models.checkout_item import CheckoutItem
from gifts.models.gift import Gift


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "amount")
    search_fields = ("name",)


@admin.register(CheckoutItem)
class CheckoutItemAdmin(admin.ModelAdmin):
    list_display = ("gift", "quantity", "total")
    search_fields = ("gift",)


class CheckoutItemInline(admin.TabularInline):
    model = CheckoutItem
    extra = 0


@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ("user", "total")
    search_fields = (
        "user__email",
        "user__username",
    )
    readonly_fields = ("total",)
    inlines = (CheckoutItemInline,)

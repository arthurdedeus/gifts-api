from django.contrib import admin

from gifts.models import Gift


# Register your models here.
@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "amount")
    search_fields = ("name",)

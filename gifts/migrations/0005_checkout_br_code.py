# Generated by Django 5.0.2 on 2024-04-14 16:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gifts", "0004_checkout_message"),
    ]

    operations = [
        migrations.AddField(
            model_name="checkout",
            name="br_code",
            field=models.CharField(
                default="", help_text="BR Code for Pix payment", max_length=1024
            ),
            preserve_default=False,
        ),
    ]

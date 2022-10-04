# Generated by Django 4.0.7 on 2022-09-20 09:40

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0156_order_tax_exemption"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="base_shipping_price_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal("0.0"), max_digits=12
            ),
        ),
    ]

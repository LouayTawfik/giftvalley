# Generated by Django 3.2 on 2022-09-28 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftcard', '0006_card_design_merchant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]

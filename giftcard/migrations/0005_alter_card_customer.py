# Generated by Django 4.1 on 2022-09-25 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('giftcard', '0004_alter_card_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='giftcard.customer'),
        ),
    ]

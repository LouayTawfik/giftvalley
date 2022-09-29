# Generated by Django 4.1 on 2022-09-22 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('merchants', '0001_initial'),
        ('giftcard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='merchants.store'),
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='merchants.address'),
        ),
        migrations.AddField(
            model_name='card_design',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='merchants.store'),
        ),
        migrations.AddField(
            model_name='card',
            name='card_design',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='giftcard.card_design'),
        ),
        migrations.AddField(
            model_name='card',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='giftcard.customer'),
        ),
        migrations.AddField(
            model_name='card',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='merchants.store'),
        ),
    ]

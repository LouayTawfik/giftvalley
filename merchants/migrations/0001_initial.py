# Generated by Django 4.1 on 2022-09-22 11:11

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_1', models.TextField(max_length=200)),
                ('line_2', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Governorate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('governorate_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=11)),
                ('address', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='merchants.address')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('ONLINE', 'ONLINE'), ('OFFLINE', 'OFFLINE')], default='OFFLINE', max_length=10)),
                ('online_store_URL', models.URLField(null=True)),
                ('address', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='merchants.address')),
                ('merchant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='store', to='merchants.merchant')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=20)),
                ('governorate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='merchants.governorate')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='merchants.city'),
        ),
    ]

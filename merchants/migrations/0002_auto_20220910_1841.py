# Generated by Django 3.2 on 2022-09-10 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchants', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='name',
            new_name='store_name',
        ),
        migrations.RemoveField(
            model_name='merchant',
            name='company',
        ),
    ]
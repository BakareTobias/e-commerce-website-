# Generated by Django 4.1 on 2022-09-28 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_bid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='user_id',
            new_name='bidder_id',
        ),
    ]
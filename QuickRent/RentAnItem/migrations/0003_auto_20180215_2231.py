# Generated by Django 2.0 on 2018-02-15 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RentAnItem', '0002_item_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='itype',
        ),
        migrations.AddField(
            model_name='item',
            name='itype',
            field=models.ManyToManyField(help_text='Select item categories', to='RentAnItem.category'),
        ),
    ]

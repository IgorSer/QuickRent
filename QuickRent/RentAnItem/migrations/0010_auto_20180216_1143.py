# Generated by Django 2.0 on 2018-02-16 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RentAnItem', '0009_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]

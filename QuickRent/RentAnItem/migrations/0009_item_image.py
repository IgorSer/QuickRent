# Generated by Django 2.0 on 2018-02-16 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RentAnItem', '0008_auto_20180216_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]

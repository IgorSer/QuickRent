# Generated by Django 2.0 on 2018-02-15 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RentAnItem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(null=True),
        ),
    ]

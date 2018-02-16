from django.db import models
from django.utils import timezone
from django.urls import reverse
import datetime
# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class item(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, default="")
    price = models.IntegerField()
    description = models.TextField(null=True)
    date_added = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank=True, null=True,upload_to='images/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('item-detail',args[str(self.id)])

    def priceFilter(fromA,toB):
        if self.price > fromA and self.price < toB:
            return self.title


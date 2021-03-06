from django.db import models
import datetime


class Historical(models.Model):
    circulating_supply = models.DecimalField(max_digits=19, decimal_places=2,
                                             default=0)
    datetime = models.DateTimeField(default=datetime.datetime.now(),
                                    blank=True)
    historical_price = models.DecimalField(max_digits=19, decimal_places=10,
                                           default=0)
    market_cap = models.DecimalField(max_digits=19, decimal_places=2,
                                     default=0)
    name = models.CharField(max_length=30, default="")
    volume = models.DecimalField(max_digits=19, decimal_places=2,
                                 default=0)

    class Meta:
        unique_together = ('name', 'datetime',)


class Prediction(models.Model):
    datetime = models.DateTimeField(default=datetime.datetime.now(),
                                    blank=True)
    name = models.CharField(max_length=30, default="")
    predicted_price = models.DecimalField(max_digits=19, decimal_places=10)


class Coin(models.Model):
    circulating_supply = models.DecimalField(max_digits=19,
                                             decimal_places=2, default=0)
    market_cap = models.DecimalField(max_digits=19,
                                     decimal_places=2, default=0)
    name = models.CharField(primary_key=True, max_length=30, default="")
    price = models.DecimalField(max_digits=19, decimal_places=10, default=0)
    rank = models.IntegerField(default=0)
    symbol = models.CharField(max_length=6, default="")
    price_change_day = models.DecimalField(max_digits=19,
                                           decimal_places=2, default=0)
    price_change_hour = models.DecimalField(max_digits=19,
                                            decimal_places=2, default=0)
    price_change_week = models.DecimalField(max_digits=19,
                                            decimal_places=2, default=0)
    volume = models.DecimalField(max_digits=19, decimal_places=2, default=0)

class Description(models.Model):
    name = models.CharField(max_length=30, default="")
    description = models.TextField(default="")

from django.db import models


class Place(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    imgs = models.TextField("Заголовок", max_length=200)
    description_short = models.CharField("Описание короткое", max_length=512)
    description_long = models.Man("Описание длинное")
    # coordinates = models.TextField("Заголовок", max_length=200)
    lat = models.FloatField(verbose_name='широта')
    lon = models.FloatField(verbose_name='долгота')

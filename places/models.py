from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    description_short = models.CharField("Описание короткое", max_length=512)
    description_long = HTMLField("Описание длинное")
    lat = models.FloatField(verbose_name='широта')
    lon = models.FloatField(verbose_name='долгота')

    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    img = models.ImageField(upload_to='images/')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='место', related_name='images')
    position = models.IntegerField(verbose_name='позиция')

    class Meta:
        ordering = ["position"]
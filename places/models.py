from django.db import models


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    description_short = models.TextField('Краткое описание',
                                         null=True,
                                         blank=True)
    description_long = models.TextField('Подробное описание',
                                        null=True,
                                        blank=True)
    lng = models.FloatField('Широта')
    lon = models.FloatField('Долгота')

    def __str__(self):
        return self.title

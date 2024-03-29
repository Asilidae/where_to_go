from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    title_short = models.CharField('Заголовок, при наведении курсора',
                                   max_length=200)
    place_id = models.CharField('ID места', max_length=20)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = HTMLField('Подробное описание', blank=True)
    lng = models.FloatField('Широта')
    lon = models.FloatField('Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place,
                              verbose_name='Место, в котором сделано фото',
                              related_name='images',
                              on_delete=models.CASCADE)
    image = models.ImageField('Изображение', blank=True)
    number = models.IntegerField('Номер по порядку')

    def get_image(self):
        if not self.image:
            return 'Картинка ещё не загружена'
        return '<img src="{url}" height={height} />'.format(
            url=self.image.url,
            height='200px'
        )

    def __str__(self):
        return '{number} {tittle}'.format(number=self.number,
                                          tittle=self.place.title)

    class Meta:
        ordering = ('number',)


class UserSelectedPlaces(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    places = models.ManyToManyField(Place)

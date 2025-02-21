from django.db import models


class Hashtag(models.Model):
    HASHTAG_CHOICE = (
        ('Детская', 'Детская'),
        ('Взрослая', 'Взрослая'),
        ('Подростковая', 'Подростковая'),
    )
    title = models.CharField(max_length=255, verbose_name='Название', choices=HASHTAG_CHOICE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Хэштег'
        verbose_name_plural = 'Хэштеги'


class Clothes(models.Model):
    HASHTAG_CHOICE = (
        ('Детская', 'Детская'),
        ('Взрослая', 'Взрослая'),
        ('Подростковая', 'Подростковая'),
    )
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.ManyToManyField(Hashtag, related_name='clothes', verbose_name='Хэштеги')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежда'
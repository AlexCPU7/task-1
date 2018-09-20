from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Model(models.Model):
    title = models.CharField('Модель', max_length=50)
    max_weight = models.IntegerField('Макс. грузоподъемность', validators=[
        MinValueValidator(1),
        MaxValueValidator(1000)
    ])
    create_dt = models.DateTimeField('Дата создания', auto_now_add=True)
    update_dt = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

    def __str__(self):
        return self.title


class Tipper(models.Model):
    number = models.CharField('Бортовой номер', max_length=50)
    model = models.ForeignKey(Model, verbose_name='Модель', on_delete=models.CASCADE)
    weight = models.IntegerField('Текущий вес', validators=[
        MinValueValidator(1),
        MaxValueValidator(1000)
    ])
    create_dt = models.DateTimeField('Дата создания', auto_now_add=True)
    update_dt = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        verbose_name = 'Самосвал'
        verbose_name_plural = 'Самосвалы'

    def __str__(self):
        return self.number

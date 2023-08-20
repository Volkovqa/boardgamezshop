from django.db import models

class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.PositiveIntegerField(verbose_name='Номер версии')
    name = models.CharField(max_length=150, verbose_name='Название версии')
    is_actual = models.BooleanField(verbose_name='Признак текущей версии')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
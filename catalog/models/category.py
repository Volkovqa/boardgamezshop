from django.db import models


NULLABLE = {
    'blank': True,
    'null': True
}

NOT_NULLABLE = {
    'blank': False,
    'null': False
}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование', **NOT_NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name} - {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name', )

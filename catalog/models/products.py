from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}

NOT_NULLABLE = {
    'blank': False,
    'null': False
}


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование', **NOT_NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='products/', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена', **NOT_NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, **NOT_NULLABLE)
    updated_at = models.DateTimeField(auto_now=True, **NOT_NULLABLE)

    def __str__(self):
        return f'{self.name} - {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name', 'price')

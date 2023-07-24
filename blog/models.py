from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}

NOT_NULLABLE = {
    'blank': False,
    'null': False
}


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='Slug')
    content = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='blog_preview/', **NULLABLE, verbose_name='Превью (изображение)')
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_count = models.PositiveIntegerField(default=0, editable=False, verbose_name='Количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

# Generated by Django 4.2.3 on 2023-07-17 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category_id',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]

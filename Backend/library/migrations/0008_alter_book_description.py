# Generated by Django 4.1.1 on 2022-09-14 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(default=None, max_length=200),
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-14 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_book_isadmin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='isAdmin',
        ),
        migrations.AddField(
            model_name='user',
            name='isAdmin',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-07 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_user_alter_book_taken'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='read_books_amount',
            field=models.IntegerField(default=0, verbose_name='Cantidad de libros leídos'),
        ),
    ]

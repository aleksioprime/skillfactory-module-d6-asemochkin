# Generated by Django 3.1.6 on 2021-02-07 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='copy_count',
            field=models.SmallIntegerField(null=True, verbose_name='Число копий'),
        ),
        migrations.AlterField(
            model_name='book',
            name='friends',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='book_friend', to='home_library.friend', verbose_name='Должник'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True, verbose_name='Цена'),
        ),
    ]
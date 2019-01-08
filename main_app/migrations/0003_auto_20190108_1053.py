# Generated by Django 2.1.3 on 2019-01-08 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20190107_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='static/images/users', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='flower',
            name='img',
            field=models.ImageField(blank=True, default='images/default.png', null=True, upload_to='static/images', verbose_name='Изображение'),
        ),
    ]
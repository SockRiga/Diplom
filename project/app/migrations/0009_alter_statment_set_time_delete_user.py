# Generated by Django 5.0.6 on 2024-06-13 10:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_user_full_name_remove_user_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statment',
            name='set_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 13, 10, 55, 54, 567474, tzinfo=datetime.timezone.utc), verbose_name='Выбрать время'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]

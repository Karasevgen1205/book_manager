# Generated by Django 3.1.3 on 2021-01-08 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='text',
            field=models.TextField(max_length=1000, null=True, verbose_name='Описание'),
        ),
    ]

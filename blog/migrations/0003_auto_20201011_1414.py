# Generated by Django 3.1.2 on 2020-10-11 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201011_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Last modified'),
        ),
    ]

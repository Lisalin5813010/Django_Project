# Generated by Django 4.2.2 on 2023-12-02 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0007_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Calculation',
        ),
        migrations.DeleteModel(
            name='PersonList',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]

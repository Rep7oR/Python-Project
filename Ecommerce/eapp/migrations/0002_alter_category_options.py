# Generated by Django 4.2.5 on 2023-09-13 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',)},
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-31 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('img', models.ImageField(upload_to='team_pic')),
                ('desc', models.TextField()),
            ],
        ),
    ]

# Generated by Django 4.2.3 on 2023-09-13 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_blogs'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='description',
            field=models.TextField(default='Default Description'),
        ),
    ]

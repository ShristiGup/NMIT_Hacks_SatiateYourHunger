# Generated by Django 3.1.7 on 2022-05-26 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20220526_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='addedrecipe',
            name='title',
            field=models.CharField(default='Syh', max_length=400),
            preserve_default=False,
        ),
    ]

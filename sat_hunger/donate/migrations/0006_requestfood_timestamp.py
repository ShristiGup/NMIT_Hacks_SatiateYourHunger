# Generated by Django 3.1.7 on 2022-05-28 09:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0005_requestfood_no_of_people'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestfood',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 5, 28, 15, 8, 27, 140864)),
            preserve_default=False,
        ),
    ]
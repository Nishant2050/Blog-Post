# Generated by Django 2.0.3 on 2018-04-13 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0006_auto_20180403_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitingplaces',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

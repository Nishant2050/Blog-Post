# Generated by Django 2.0.3 on 2018-04-02 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0003_auto_20180331_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitingplaces',
            name='state',
        ),
        migrations.AddField(
            model_name='visitingplaces',
            name='country',
            field=models.ForeignKey(default='India', on_delete=django.db.models.deletion.CASCADE, related_name='vplaces', to='chatapp.Country'),
            preserve_default=False,
        ),
    ]

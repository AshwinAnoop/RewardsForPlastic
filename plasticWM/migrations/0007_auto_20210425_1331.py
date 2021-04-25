# Generated by Django 3.1.7 on 2021-04-25 13:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('plasticWM', '0006_disposal_disposaldone'),
    ]

    operations = [
        migrations.AddField(
            model_name='disposal',
            name='disposaldate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='extendeduser',
            name='is_pickperson',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='extendeduser',
            name='is_shopowner',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pickup',
            name='pickupdate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
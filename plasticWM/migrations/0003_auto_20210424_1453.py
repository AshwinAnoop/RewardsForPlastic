# Generated by Django 3.1.7 on 2021-04-24 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plasticWM', '0002_extendeduser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapshop',
            name='locality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plasticWM.locality'),
        ),
    ]

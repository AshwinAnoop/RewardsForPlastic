# Generated by Django 3.1.7 on 2021-04-24 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plasticWM', '0003_auto_20210424_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapshop',
            name='locality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='plasticWM.locality'),
        ),
    ]
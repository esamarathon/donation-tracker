# Generated by Django 2.0.4 on 2018-05-29 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_add_horaro_twitch_tiltify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='bidsuggestion',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Name'),
        ),
    ]

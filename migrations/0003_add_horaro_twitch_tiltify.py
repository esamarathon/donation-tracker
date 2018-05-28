# Generated by Django 2.0.5 on 2018-05-28 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_add_country_records'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='horaro_category_col',
            field=models.IntegerField(blank=True, help_text='Column index for category info (start at 0)', null=True, verbose_name='Category Column'),
        ),
        migrations.AddField(
            model_name='event',
            name='horaro_commentators_col',
            field=models.IntegerField(blank=True, help_text='Column index for commentator info (start at 0)', null=True, verbose_name='Commentators Column'),
        ),
        migrations.AddField(
            model_name='event',
            name='horaro_game_col',
            field=models.IntegerField(blank=True, help_text='Column index for game info (start at 0)', null=True, verbose_name='Game Column'),
        ),
        migrations.AddField(
            model_name='event',
            name='horaro_id',
            field=models.CharField(blank=True, default='', help_text='ID or slug for Horaro event', max_length=100, verbose_name='Event ID'),
        ),
        migrations.AddField(
            model_name='event',
            name='horaro_runners_col',
            field=models.IntegerField(blank=True, help_text='Column index for runner info (start at 0)', null=True, verbose_name='Runners Column'),
        ),
        migrations.AddField(
            model_name='event',
            name='tiltify_api_key',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Tiltify Campaign API Key'),
        ),
        migrations.AddField(
            model_name='event',
            name='tiltify_enable_sync',
            field=models.BooleanField(default=False, help_text='Sync donations for this event via the Tiltify API', verbose_name='Enable Tiltify Sync'),
        ),
        migrations.AddField(
            model_name='event',
            name='twitch_channel',
            field=models.CharField(blank=True, default='', help_text='Announcements will be made to this channel', max_length=100, verbose_name='Channel Name'),
        ),
        migrations.AddField(
            model_name='event',
            name='twitch_login',
            field=models.CharField(blank=True, default='', help_text='Username to use for chat announcements', max_length=100, verbose_name='Username'),
        ),
        migrations.AddField(
            model_name='event',
            name='twitch_oauth',
            field=models.CharField(blank=True, default='', help_text='Get one here: http://www.twitchapps.com/tmi', max_length=200, verbose_name='OAuth Password'),
        ),
        migrations.AddField(
            model_name='prize',
            name='auto_tickets',
            field=models.BooleanField(default=False, help_text='Counts all qualifying donations towards tickets automatically', verbose_name='Automatic Tickets'),
        ),
    ]

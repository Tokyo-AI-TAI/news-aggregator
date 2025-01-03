# Generated by Django 5.0.9 on 2024-12-14 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed_service', '0004_rename_content_to_full_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedentry',
            name='content_translated',
        ),
        migrations.RemoveField(
            model_name='feedentry',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='feedentry',
            name='translation_language',
        ),
        migrations.AddField(
            model_name='userfeedsubscription',
            name='custom_summary',
            field=models.TextField(blank=True, default='', help_text="Custom summary, translated into the user's language, of the feed for the user based on their interests"),
        ),
        migrations.AddField(
            model_name='userfeedsubscription',
            name='relevance_score',
            field=models.IntegerField(default=0, help_text='Relevance score of the feed for the user based on their interests, from 0 to 100'),
        ),
    ]

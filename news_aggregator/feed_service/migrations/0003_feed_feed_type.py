# Generated by Django 5.0.9 on 2024-12-07 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed_service', '0002_alter_feedentry_content_translated_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='feed_type',
            field=models.CharField(choices=[('rss', 'RSS Feed'), ('website', 'Website')], default='rss', help_text='Type of feed source', max_length=10),
        ),
    ]

# Generated by Django 5.0.9 on 2024-12-07 06:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed_service', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedentry',
            name='content_translated',
            field=models.TextField(blank=True, default='', help_text='AI-translated content'),
        ),
        migrations.AlterField(
            model_name='feedentry',
            name='summary',
            field=models.TextField(blank=True, default='', help_text='AI-generated summary of the content'),
        ),
        migrations.AlterField(
            model_name='feedentry',
            name='title_translated',
            field=models.CharField(blank=True, default='', help_text='AI-translated title', max_length=200),
        ),
        migrations.AlterField(
            model_name='feedentry',
            name='translation_language',
            field=models.CharField(blank=True, default='', help_text='Language code of the translation', max_length=10),
        ),
        migrations.CreateModel(
            name='UserFeedSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribed_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribers', to='feed_service.feed')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feed_subscriptions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-subscribed_at'],
                'unique_together': {('user', 'feed')},
            },
        ),
    ]
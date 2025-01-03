from django.db import models
from django.utils import timezone


class Feed(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(unique=True)
    description = models.TextField(blank=True)
    last_updated = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    FEED_TYPE_RSS = "rss"
    FEED_TYPE_WEBSITE = "website"
    FEED_TYPE_CHOICES = [
        (FEED_TYPE_RSS, "RSS Feed"),
        (FEED_TYPE_WEBSITE, "Website"),
    ]
    feed_type = models.CharField(
        max_length=10,
        choices=FEED_TYPE_CHOICES,
        default=FEED_TYPE_RSS,
        help_text="Type of feed source",
    )

    class Meta:
        app_label = "feed_service"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class FeedEntry(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name="entries")
    title = models.CharField(max_length=200)
    url = models.URLField()
    full_content = models.TextField(
        help_text="Full content of the article. Initially contains feed summary, later updated with full article text"
    )
    article_load_error = models.TextField(
        blank=True, default="", help_text="Error message if article loading failed"
    )
    article_loaded_at = models.DateTimeField(
        null=True, blank=True, help_text="When the full article was loaded"
    )
    author = models.CharField(max_length=100, blank=True)
    published_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    # AI-generated fields
    last_processed = models.DateTimeField(
        null=True,
        blank=True,
        help_text="When the entry was last processed by AI",
    )

    class Meta:
        ordering = ["-published_at"]
        verbose_name_plural = "Feed entries"

    def __str__(self):
        return self.title


class UserFeedSubscription(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="feed_subscriptions"
    )
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name="subscribers")
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ["user", "feed"]
        ordering = ["-subscribed_at"]

    def __str__(self):
        return f"{self.user.username} - {self.feed.title}"


class UserArticleInteraction(models.Model):
    """Stores AI-generated content and user-specific data for each article."""

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="article_interactions"
    )
    entry = models.ForeignKey(
        FeedEntry, on_delete=models.CASCADE, related_name="user_interactions"
    )
    custom_summary = models.TextField(
        blank=True,
        default="",
        help_text="AI-generated summary of the article customized for the user",
    )
    translated_title = models.CharField(
        max_length=200,
        blank=True,
        default="",
        help_text="AI-translated or improved title in English",
    )
    relevance_score = models.IntegerField(
        default=0,
        help_text="AI-generated relevance score for the user, from 0 to 100",
    )
    processed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["user", "entry"]
        ordering = ["-processed_at"]

    def __str__(self):
        return f"{self.user.username} - {self.entry.title}"

from django.db import models

class RSSFeed(models.Model):
    category = models.CharField(max_length=200)  # First two words
    url = models.URLField(unique=True)  # Third word (RSS link)
    created_at = models.DateTimeField(auto_now_add=True)
    last_fetched = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.category} - {self.url}"

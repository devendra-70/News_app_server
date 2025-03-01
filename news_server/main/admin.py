from django.contrib import admin
from .models import RSSFeed  # Only import the existing model

@admin.register(RSSFeed)
class RSSFeedAdmin(admin.ModelAdmin):
    list_display = ("category", "url", "created_at", "last_fetched", "active")
    search_fields = ("category", "url")
    list_filter = ("category", "active")

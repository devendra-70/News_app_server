import os
import sys
import django

# Set up Django environment
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_server.settings")
django.setup()

from main.models import RSSFeed

# File path for RSS links
RSS_FILE_PATH = "main/scripts/rss-urls-1.txt"

def parse_rss_file(file_path):
    """Reads the file and extracts category and RSS URL"""
    feeds = []
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split()  # Splitting by space
                
                if len(parts) < 3:
                    print(f"Skipping invalid line: {line.strip()}")
                    continue
                
                category = " ".join(parts[:2])  # First two words as category
                url = parts[2]  # Third word as RSS link
                
                feeds.append((category, url))
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

    return feeds

def bulk_import_feeds():
    """Bulk imports RSS feeds into the database"""
    feeds = parse_rss_file(RSS_FILE_PATH)
    
    if not feeds:
        print("No valid feeds found. Exiting.")
        return
    
    for category, url in feeds:
        try:
            obj, created = RSSFeed.objects.get_or_create(category=category, url=url)
            if created:
                print(f"✅ Added: {category} -> {url}")
            else:
                print(f"⚠️ Already exists: {category} -> {url}")
        except Exception as e:
            print(f"❌ Error inserting {category} -> {url}: {e}")

if __name__ == "__main__":
    bulk_import_feeds()
    print("✅ RSS Feed Import Complete!")

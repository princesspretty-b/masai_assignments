import requests
import time
import json
import os
from datetime import datetime

# Base URLs for HackerNews API
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# Header required by assignment
headers = {"User-Agent": "TrendPulse/1.0"}

# Category keywords (case-insensitive matching)
CATEGORIES = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

def fetch_top_story_ids():
    """Fetch top story IDs from HackerNews"""
    try:
        response = requests.get(TOP_STORIES_URL, headers=headers)
        response.raise_for_status()
        return response.json()[:500]  # take first 500
    except Exception as e:
        print(f"Error fetching top stories: {e}")
        return []

def fetch_story(story_id):
    """Fetch a single story by ID"""
    try:
        response = requests.get(ITEM_URL.format(story_id), headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Failed to fetch story {story_id}: {e}")
        return None

def categorize_title(title):
    """Assign category based on keywords"""
    if not title:
        return None

    title_lower = title.lower()

    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in title_lower:
                return category
    return None  # ignore if no category matched

story_ids = fetch_top_story_ids()
print(story_ids)
collected_data = []
category_counts = {cat: 0 for cat in CATEGORIES}
print(category_counts)
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(current_time)

# Loop category-wise (as required)
for category in CATEGORIES:
    print(f"Collecting category: {category}")

    for story_id in story_ids:
        # Stop if we already have 25 stories in this category
        if category_counts[category] >= 25:
            break
        story = fetch_story(story_id)
        if not story:
            continue

        title = story.get("title", "")
        detected_category = categorize_title(title)

        # Only collect if it matches current category
        if detected_category != category:
            continue

        # Extract required fields
        data = {
            "post_id": story.get("id"),
            "title": title,
            "category": category,
            "score": story.get("score", 0),
            "num_comments": story.get("descendants", 0),
            "author": story.get("by", "unknown"),
             "collected_at": current_time
        }

        collected_data.append(data)
        category_counts[category] += 1

    # Wait 2 seconds AFTER finishing one category
    time.sleep(2)

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Create filename with date
filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

# Save to JSON
with open(filename, "w", encoding="utf-8") as f:
    json.dump(collected_data, f, indent=4)

print(f"Collected {len(collected_data)} stories. Saved to {filename}")

#!/usr/bin/env python3
"""
Download professional project images for portfolio
"""

import os
import urllib.request
import urllib.error
from pathlib import Path

# Create directories if they don't exist
profile_dir = Path("assets/profile")
projects_dir = Path("assets/projects")

profile_dir.mkdir(parents=True, exist_ok=True)
projects_dir.mkdir(parents=True, exist_ok=True)

print("=" * 60)
print("Downloading Professional Portfolio Images")
print("=" * 60)

# Professional project images from Unsplash (free, high quality)
images = {
    "assets/projects/project1.jpg": "https://images.unsplash.com/photo-1557821552-17105176677c?w=800&q=80",  # E-Commerce
    "assets/projects/project2.jpg": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&q=80",  # Task Management
    "assets/projects/project3.jpg": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&q=80",  # Portfolio
}

# Professional profile image
profile_image = {
    "assets/profile/profile.jpg": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&q=80",  # Professional headshot
}

# Download profile image
print("\n📸 Downloading profile image...")
for filepath, url in profile_image.items():
    try:
        print(f"   Downloading: {filepath}")
        urllib.request.urlretrieve(url, filepath)
        print(f"   ✅ Success: {filepath}")
    except urllib.error.URLError as e:
        print(f"   ❌ Error downloading {filepath}: {e}")
    except Exception as e:
        print(f"   ❌ Unexpected error: {e}")

# Download project images
print("\n🖼️  Downloading project images...")
for filepath, url in images.items():
    try:
        print(f"   Downloading: {filepath}")
        urllib.request.urlretrieve(url, filepath)
        print(f"   ✅ Success: {filepath}")
    except urllib.error.URLError as e:
        print(f"   ❌ Error downloading {filepath}: {e}")
    except Exception as e:
        print(f"   ❌ Unexpected error: {e}")

print("\n" + "=" * 60)
print("✅ Download Complete!")
print("=" * 60)
print("\nYour portfolio images have been downloaded successfully!")
print("\nNext steps:")
print("1. Open index.html in your browser")
print("2. View your portfolio with professional images")
print("3. Customize the content as needed")
print("\nNote: These are sample images from Unsplash.")
print("You can replace them with your own images anytime.")
print("=" * 60)

# ubuntu_image_fetcher.py
"""
Ubuntu-Inspired Image Fetcher
"I am because we are" 🌍

This script:
- Prompts user for an image URL
- Downloads the image with respect and care
- Saves it to 'Fetched_Images' directory
- Handles errors gracefully
"""

import os
import requests
from urllib.parse import urlparse
import uuid

def fetch_image():
    url = input("🌐 Please enter an image URL: ").strip()

    # Create directory if not exists
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    try:
        # Request the image
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise HTTPError for bad status codes

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename, generate one
        if not filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"

        filepath = os.path.join(folder, filename)

        # Save the image in binary mode
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"✅ Image saved as: {filepath}")

    except requests.exceptions.MissingSchema:
        print("❌ Invalid URL format. Please include http:// or https://")
    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"❌ Network error occurred: {err}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    fetch_image()

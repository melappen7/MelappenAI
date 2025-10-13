import random
import requests
from PIL import Image
from io import BytesIO

# Data source: In a real-world scenario, you would scrape from a website.
# Here, we simulate it with a list of image URLs and words.
IMAGE_DATA = [
    ('cat', 'https://via.placeholder.com/150/0000FF/FFFFFF?text=Cat'),
    ('dog', 'https://via.placeholder.com/150/FF0000/FFFFFF?text=Dog'),
    ('bird', 'https://via.placeholder.com/150/008000/FFFFFF?text=Bird'),
    ('house', 'https://via.placeholder.com/150/FFFF00/000000?text=House'),
    ('tree', 'https://via.placeholder.com/150/00FF00/000000?text=Tree')
]

def fetch_random_image_and_word():
    """
    Fetches a random image URL and its corresponding word from the data source.
    Downloads the image and returns both the word and the image object.
    """
    try:
        word, image_url = random.choice(IMAGE_DATA)
        print(f"Fetching data for: '{word}'...")
        response = requests.get(image_url)
        response.raise_for_status() # Raise an error for bad responses
        image = Image.open(BytesIO(response.content))
        return image, word
    except requests.exceptions.RequestException as e:
        print(f"Error fetching image from URL: {e}")
        return None, None

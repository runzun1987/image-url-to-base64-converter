from typing import Tuple
from PIL import Image
import base64
import requests
from io import BytesIO


def convert_image_url_to_base64(
    image_url: str,
    max_size: Tuple[int, int],
    image_format: str,
    quality: int
) -> str:
    try:
        response = requests.get(image_url)
        response.raise_for_status()

        img = Image.open(BytesIO(response.content))
        img.thumbnail(max_size)  # Resize while maintaining aspect ratio

        buffer = BytesIO()
        img.save(buffer, format=image_format, quality=quality, optimize=True)
        buffer.seek(0)

        encoded_string = base64.b64encode(buffer.read()).decode('utf-8')
        return "data:image/jpeg;base64," + encoded_string
    except Exception as e:
        raise ValueError(f"Failed to convert image from URL to base64: {e}")

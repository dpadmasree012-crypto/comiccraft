import os
import requests
import uuid
from urllib.parse import quote

POLLINATIONS_URL = "https://image.pollinations.ai/prompt/"


def generate_image(prompt: str, width: int = 768, height: int = 768) -> str:
    """Generate an image using Pollinations.ai (free, no API key)."""
    os.makedirs("static/panels", exist_ok=True)
    filename = f"{uuid.uuid4().hex}.png"
    filepath = os.path.join("static", "panels", filename)

    url = f"{POLLINATIONS_URL}{quote(prompt)}?width={width}&height={height}&nologo=true"

    try:
        response = requests.get(url, timeout=120)
        response.raise_for_status()
        with open(filepath, "wb") as f:
            f.write(response.content)
        return filepath.replace("\\", "/")
    except Exception as e:
        print(f"Image generation failed: {e}")
        return None
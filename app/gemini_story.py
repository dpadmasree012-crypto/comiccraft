import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()
MODEL_NAME = "gemini-3.8-flash"


def generate_story(panels):
    """Generate full narration and dialogue from the panel outline."""
    outline_text = "\n".join([
        f"Panel {p.get('panel')}: {p.get('title')} — {p.get('scene_description')}"
        for p in panels if "error" not in p
    ])

    prompt = f"""You are a comic book writer.
Given the following panel breakdown, write a comic-style story with engaging narration and character dialogue.

Panel outline:
{outline_text}

Guidelines:
- Use a fun and engaging tone, like a real comic book.
- Include narration and clearly marked character lines.
- Format each panel's section starting with "**Panel X:**" so it can be split later.
- Keep each panel self-contained but part of a cohesive story."""

    try:
        interaction = client.interactions.create(model=MODEL_NAME, input=prompt)
        return interaction.output_text.strip()
    except Exception as e:
        return f"Error generating story: {str(e)}"
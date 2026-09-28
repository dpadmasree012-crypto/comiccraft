import os
import json
import re
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()
MODEL_NAME = "gemini-3.8-flash"


def generate_outline(user_prompt):
    """Generate a 5-panel comic outline."""
    prompt = f"""You are a professional AI comic planner.
Generate a STRICTLY FORMATTED JSON array containing 5 panel descriptions for a comic based on this story idea:

STORY: {user_prompt}

Each JSON object MUST include:
- "panel" (integer, 1 to 5)
- "title" (short string)
- "scene_description" (1-2 sentences)
- "image_prompt" (detailed visual prompt for an image generator, in English, describing the scene, characters, colors, and art style)

Respond ONLY in valid JSON. Do NOT include markdown fences or explanations."""

    try:
        interaction = client.interactions.create(model=MODEL_NAME, input=prompt)
        raw = interaction.output_text.strip()
        raw = re.sub(r"```json|```", "", raw).strip()
        match = re.search(r"\[.*\]", raw, re.DOTALL)
        if match:
            raw = match.group(0)
        panels = json.loads(raw)
        return panels
    except Exception as e:
        return [{"error": f"Outline generation failed: {str(e)}"}]
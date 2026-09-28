import os
import re
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.gemini_outline import generate_outline
from app.gemini_story import generate_story
from app.image_generator import generate_image

app = FastAPI(title="ComicCraft")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def split_story_by_panel(full_story: str, num_panels: int):
    """Split the full story text into individual panels using '**Panel X' markers."""
    pattern = re.compile(r"\*\*Panel\s*\d+.*?(?=\*\*Panel\s*\d+|$)", re.DOTALL | re.IGNORECASE)
    sections = pattern.findall(full_story)

    if len(sections) != num_panels:

        
        words = full_story.split()
        chunk = max(1, len(words) // num_panels)
        sections = [" ".join(words[i * chunk:(i + 1) * chunk]) for i in range(num_panels)]

    cleaned = []
    for s in sections:
        s = s.strip()
        s = re.sub(r"^\*\*Panel\s*\d+[:\-]?\s*", "", s, flags=re.IGNORECASE).strip()
        cleaned.append(s)
    return cleaned


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.post("/generate", response_class=HTMLResponse)
async def generate(
    request: Request,
    prompt: str = Form(...),
    character_name: str = Form(...),
    setting: str = Form(...),
    tone: str = Form(...),
    style: str = Form(...)
):
    full_prompt = (
        f"{prompt}. Main character: {character_name}. "
        f"Setting: {setting}. Tone: {tone}. Art style: {style}."
    )

    panels = generate_outline(full_prompt)

    if not panels or "error" in panels[0]:
        return templates.TemplateResponse(request=request, name="comic_preview.html", context={
            "layout": [],
            "error": panels[0].get("error", "Unknown error") if panels else "Failed to generate outline."
        })

    full_story = generate_story(panels)
    story_chunks = split_story_by_panel(full_story, len(panels))

    layout = []
    for i, panel in enumerate(panels):
        image_prompt = panel.get("image_prompt", f"Comic panel: {panel.get('scene_description', '')}")
        image_path = generate_image(image_prompt)

        layout.append({
            "panel": panel.get("panel", i + 1),
            "title": panel.get("title", f"Panel {i + 1}"),
            "scene_description": panel.get("scene_description", ""),
            "image_path": "/" + image_path if image_path else None,
            "text": story_chunks[i] if i < len(story_chunks) else full_story,
        })

    return templates.TemplateResponse(request=request, name="comic_preview.html", context={
        "layout": layout,
        "error": None
    })
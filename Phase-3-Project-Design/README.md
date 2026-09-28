# Phase 3: Project Design

- **Architecture Flow:**
  User Browser → FastAPI Backend (`main.py`)
  → `gemini_outline.generate_outline()` (panel structure)
  → `gemini_story.generate_story()` (story text per panel)
  → `image_generator.generate_image()` (image per panel)
  → FastAPI Backend → User Browser (`comic_preview.html`)

- **UI Design:**
  - **Page 1 (`index.html`):** Comic creation form — prompt, character name, setting, tone, art style.
  - **Page 2 (`comic_preview.html`):** Rendered comic grid with panel images, titles, and story text.
  - Clean typography, card-style panels, and a prominent "Create Another Comic" link.

- **Folder Structure:**
  - `app/` — backend logic (`main.py`, `gemini_outline.py`, `gemini_story.py`, `image_generator.py`, `exporters.py`)
  - `templates/` — Jinja2 HTML templates
  - `static/` — CSS, generated panel images, and exports
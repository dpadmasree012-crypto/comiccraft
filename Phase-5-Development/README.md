# Phase 5: Development

- Built a FastAPI backend (`app/main.py`) with two routes:
  - `GET /` — renders the comic creation form.
  - `POST /generate` — accepts the form, generates the comic, and renders the preview.
- Integrated the Google Gemini API for:
  - **Outline generation** — breaks the prompt into panels.
  - **Story generation** — writes narrative text for each panel.
- Integrated an AI image generator to create one image per panel.
- Used Jinja2 templating to render dynamic HTML from backend data.
- Served static assets (CSS + generated images) via `StaticFiles`.
- Secured the API key using a `.env` file and `python-dotenv`.
- Added a helper `split_story_by_panel()` to align story text with panel images.
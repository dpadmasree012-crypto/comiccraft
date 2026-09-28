# 🎨 ComicCraft: AI Comic Story Creator using Gemini Models

ComicCraft is a web-based application that turns a simple text prompt into a fully illustrated, multi-panel comic book using Google Gemini for story generation and Pollinations.ai for free AI illustrations.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688)
![Gemini](https://img.shields.io/badge/Google-Gemini%20API-4285F4)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

* **🧠 AI Story Generation** — Gemini creates a structured 5-panel comic outline and full narration for each panel.
* **🖼️ AI Illustrations** — Free, no-API-key image generation via [Pollinations.ai](https://pollinations.ai).
* **🎭 Style Control** — Choose your character, setting, tone, and art style.
* **📄 PDF Export** — Download your finished comic as a PDF using `fpdf2`.
* **💻 Clean UI** — Simple form-based flow from prompt → comic preview.

---

## 🛠️ Tech Stack

| Layer      | Technology                                  |
| ---------- | ------------------------------------------- |
| Backend    | FastAPI, Uvicorn, Python 3.10+              |
| Frontend   | HTML, CSS, Jinja2                           |
| AI Text    | Google Gemini API (`gemini-2.5-flash`)      |
| AI Images  | Pollinations.ai (free, no API key required) |
| PDF Export | fpdf2                                       |

---

## 📂 Project Structure

```text
comiccraft/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app + routes
│   ├── gemini_outline.py       # Panel outline generation
│   ├── gemini_story.py         # Per-panel story narration
│   ├── image_generator.py      # Pollinations.ai image generation
│   └── exporters.py            # PDF export logic
├── templates/
│   ├── index.html              # Comic creation form
│   └── comic_preview.html      # Rendered comic page
├── static/
│   ├── style.css
│   ├── panels/                 # Generated panel images
│   └── exports/                # Generated PDFs
├── Phase-1-Brainstorming/
├── Phase-2-Requirement-Analysis/
├── Phase-3-Project-Design/
├── Phase-4-Project-Planning/
├── Phase-5-Development/
├── Phase-6-Testing/
├── Phase-7-Documentation/
├── Phase-8-Demonstration/
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/dpadmasree012-crypto/comiccraft.git
cd comiccraft
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

**Windows (PowerShell):**

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate
```

**Windows (CMD):**

```cmd
venv\Scripts\activate.bat
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

Get a free key from [Google AI Studio](https://aistudio.google.com/apikey).

### 5. Run the app

```bash
uvicorn app.main:app --reload
```

### 6. Open in browser

```text
http://127.0.0.1:8000
```

---

## 🖼️ How It Works

```text
User Browser
     │
     ▼
POST /generate
(prompt, character, setting, tone, style)
     │
     ▼
┌──────────────────────────────────────────────┐
│                                              │
│  gemini_outline.generate_outline()           │
│       → 5-panel structured outline            │
│                                              │
│  gemini_story.generate_story()               │
│       → Full narration text per panel        │
│                                              │
│  image_generator.generate_image()            │
│       → Pollinations.ai illustration         │
│         per panel                            │
│                                              │
└──────────────────────────────────────────────┘
     │
     ▼
Render templates/comic_preview.html
     │
     ▼
Comic Preview + PDF Export
```

---

## ⚠️ Known Limitations

* **Free-tier Gemini limits** — The free tier allows a limited number of requests per day. If you receive HTTP 429 errors, wait for the quota to reset or check your API tier.
* **Image quality** — Pollinations.ai is free but image quality can vary depending on the prompt.
* **Panel count** — Currently fixed at 5 panels per comic.
* **Internet connection** — AI story and image generation require an active internet connection.

---

## 📚 Documentation

Phase-wise documentation is available in the `Phase-*/` folders:

1. [Phase 1 — Brainstorming](./Phase-1-Brainstorming/README.md)
2. [Phase 2 — Requirement Analysis](./Phase-2-Requirement-Analysis/README.md)
3. [Phase 3 — Project Design](./Phase-3-Project-Design/README.md)
4. [Phase 4 — Project Planning](./Phase-4-Project-Planning/README.md)
5. [Phase 5 — Development](./Phase-5-Development/README.md)
6. [Phase 6 — Testing](./Phase-6-Testing/README.md)
7. [Phase 7 — Documentation](./Phase-7-Documentation/README.md)
8. [Phase 8 — Demonstration](./Phase-8-Demonstration/README.md)

---

## 🤝 Contributing

Pull requests are welcome.

For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 🙏 Acknowledgements

* [Google Gemini API](https://ai.google.dev/) — Text generation
* [Pollinations.ai](https://pollinations.ai/) — Free AI image generation
* [FastAPI](https://fastapi.tiangolo.com/) — Backend framework
* [fpdf2](https://py-pdf.github.io/fpdf2/) — PDF generation

---

## 🔧 Key Changes

| Change                                                   | Why                                              |
| -------------------------------------------------------- | ------------------------------------------------ |
| Fixed model name `gemini-3.8-flash` → `gemini-2.5-flash` | `gemini-3.8-flash` does not exist                |
| Added badges at the top                                  | Makes the repository look professional           |
| Added Project Structure                                  | Helps users understand the repository            |
| Added How It Works diagram                               | Explains the application flow                    |
| Added Known Limitations                                  | Clearly explains free-tier and image limitations |
| Added Documentation links                                | Connects all 8 project phases                    |
| Added License and Acknowledgements                       | Standard open-source sections                    |
| Specified Python 3.10+                                   | Avoids Python version confusion                  |

---

## 📤 How to Push This to GitHub

In your project root:

```powershell
git add README.md
git commit -m "Improve README with badges, structure, and phase links"
git push
```

If `.env.example` does not already exist, create it with:

```powershell
"GEMINI_API_KEY=your_key_here" | Out-File -Encoding utf8 .env.example
```

Then push it:

```powershell
git add .env.example
git commit -m "Add .env.example template"
git push
```

> **Important:** Never upload your real `.env` file or your actual Gemini API key to GitHub.

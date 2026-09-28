# Phase 7: Documentation

## How to Run ComicCraft Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/dpadmasree012-crypto/comiccraft.git
   cd comiccraft
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate it:
   - Windows (PowerShell):
     ```powershell
     Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
     .\venv\Scripts\Activate
     ```
   - Windows (CMD):
     ```cmd
     venv\Scripts\activate.bat
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the project root and add:
   ```
   GEMINI_API_KEY=your_key_here
   ```

6. Run the app:
   ```bash
   uvicorn app.main:app --reload
   ```

7. Open your browser at:
   ```
   http://127.0.0.1:8000
   ```

## Notes
- Ensure the `static/` and `templates/` folders exist before starting the server.
- Free-tier Gemini limits apply (e.g., 20 requests/day on `gemini-3.8-flash`). Upgrade or switch models if you hit HTTP 429 errors.
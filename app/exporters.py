import os
from datetime import datetime
from fpdf import FPDF


class ComicPDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 10, "ComicCraft", ln=True, align="C")
        self.ln(5)


def save_pdf(layout, title="My Comic"):
    """Compile the comic layout into a PDF and return the file path."""
    os.makedirs("static/exports", exist_ok=True)

    pdf = ComicPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    for panel in layout:
        pdf.add_page()

        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, f"Panel {panel['panel']}: {panel.get('title', '')}", ln=True, align="C")
        pdf.ln(3)

        image_path = panel.get("image_path")
        if image_path and os.path.exists(image_path):
            try:
                pdf.image(image_path, x=15, w=pdf.w - 30)
                pdf.ln(5)
            except Exception as e:
                pdf.set_font("Helvetica", "I", 10)
                pdf.multi_cell(0, 6, f"[Image could not be added: {e}]")
        else:
            pdf.set_font("Helvetica", "I", 10)
            pdf.multi_cell(0, 6, "[Image not available]")

        pdf.ln(5)

        pdf.set_font("Helvetica", size=11)
        text = panel.get("text", "No narration available.")
        text = text.replace("**", "").replace("*", "")
        pdf.multi_cell(0, 7, text)

    filename = f"comic_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    filepath = os.path.join("static", "exports", filename)
    pdf.output(filepath)
    return filepath.replace("\\", "/")
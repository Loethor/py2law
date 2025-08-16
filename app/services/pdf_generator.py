from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from docx import Document


def convert_docx_to_pdf(docx_path, pdf_path):
    """
    Converts a .docx file to a .pdf file.

    Args:
        docx_path (str): The path to the input .docx file.
        pdf_path (str): The path to the output .pdf file.

    Returns:
        bool: True if the conversion is successful, False otherwise.
    """
    try:
        # Load the .docx file
        document = Document(docx_path)

        # Create a PDF canvas
        pdf = canvas.Canvas(pdf_path, pagesize=letter)
        width, height = letter

        # Add content from the .docx file to the PDF
        y = height - 50  # Start from the top of the page
        for paragraph in document.paragraphs:
            if y < 50:  # If the page is full, create a new page
                pdf.showPage()
                y = height - 50
            pdf.drawString(50, y, paragraph.text)
            y -= 20  # Move down for the next line

        # Save the PDF
        pdf.save()
        return True
    except Exception as e:
        print(f"Error converting .docx to .pdf: {e}")
        return False

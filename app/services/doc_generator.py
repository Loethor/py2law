from docx import Document
from docx.shared import Pt


def create_docx(file_path):
    """
    Creates a .docx file with sample content.

    Args:
        file_path (str): The full path where the .docx file will be saved.
    """
    # Create a new Word document
    document = Document()

    # Add a title
    document.add_heading("Documento de Ejemplo", level=1)

    # Add some sample content
    document.add_paragraph("Este es un documento de ejemplo generado automáticamente.")
    document.add_paragraph("Puedes personalizar este contenido según tus necesidades.")

    # Add a styled paragraph
    paragraph = document.add_paragraph("Texto con estilo: ")
    run = paragraph.add_run("Este texto tiene un tamaño de fuente personalizado.")
    run.font.size = Pt(12)

    # Save the document to the specified path
    try:
        document.save(file_path)
        return True
    except Exception as e:
        print(f"Error saving document: {e}")
        return False

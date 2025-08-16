from app.services.pdf_generator import convert_docx_to_pdf
from app.services.doc_generator import create_docx


def test_convert_docx_to_pdf(tmp_path):
    """
    Test the convert_docx_to_pdf function to ensure it converts a .docx file to a .pdf file.
    """
    # Create a test .docx file
    docx_path = tmp_path / "test_document.docx"
    create_docx(str(docx_path))

    # Define the path for the test .pdf file
    pdf_path = tmp_path / "test_document.pdf"

    # Call the convert_docx_to_pdf function
    success = convert_docx_to_pdf(str(docx_path), str(pdf_path))

    # Assert that the function returns True
    assert success, "convert_docx_to_pdf should return True on success"

    # Assert that the PDF file was created
    assert pdf_path.exists(), "The .pdf file should be created"

    # Assert that the PDF file is not empty
    assert pdf_path.stat().st_size > 0, "The .pdf file should not be empty"

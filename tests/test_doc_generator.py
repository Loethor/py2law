from app.services.doc_generator import create_docx


def test_create_docx(tmp_path):
    """
    Test the create_docx function to ensure it creates a valid .docx file.
    """
    # Define the path for the test .docx file
    test_file_path = tmp_path / "test_document.docx"

    # Call the create_docx function
    success = create_docx(str(test_file_path))

    # Assert that the function returns True
    assert success, "create_docx should return True on success"

    # Assert that the file was created
    assert test_file_path.exists(), "The .docx file should be created"

    # Assert that the file is not empty
    assert test_file_path.stat().st_size > 0, "The .docx file should not be empty"

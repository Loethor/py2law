from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QFileDialog,
    QMessageBox,
)
import sys
from services.doc_generator import create_docx
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generador de Documentos")
        self.setGeometry(300, 300, 400, 200)

        # Main layout
        layout = QVBoxLayout()

        # Button to create a .docx file
        self.create_docx_button = QPushButton("Crear archivo .docx")
        self.create_docx_button.clicked.connect(self.create_docx)
        layout.addWidget(self.create_docx_button)

        # Button to convert .docx to .pdf
        self.convert_to_pdf_button = QPushButton("Convertir .docx a .pdf")
        self.convert_to_pdf_button.clicked.connect(self.convert_to_pdf)
        layout.addWidget(self.convert_to_pdf_button)

        # Central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def create_docx(self):
        # Get the user's "Documentos" folder
        default_folder = os.path.join(os.path.expanduser("~"), "Documents")

        # Open a folder dialog to let the user choose where to save the file
        folder_path = QFileDialog.getExistingDirectory(
            self, "Seleccionar carpeta para guardar el archivo", default_folder
        )
        if folder_path:
            # Append the default file name to the selected folder
            file_path = os.path.join(folder_path, "archivo_ejemplo.docx")

            # Call the create_docx function
            success = create_docx(file_path)
            if success:
                QMessageBox.information(
                    self,
                    "Éxito",
                    f"¡Archivo .docx creado exitosamente en:\n{file_path}!",
                )
            else:
                QMessageBox.critical(
                    self, "Error", "Hubo un error al crear el archivo .docx."
                )

    def convert_to_pdf(self):
        # Open a file dialog to select a .docx file
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar archivo .docx", "", "Documentos Word (*.docx)"
        )  # Dialog text in Spanish
        if file_path:
            # Placeholder for .pdf conversion logic
            QMessageBox.information(
                self, "Información", f"¡Convertir {file_path} a .pdf!"
            )  # Message in Spanish
            # You can call a function from `services/pdf_generator.py` here.


# Entry point for the application
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

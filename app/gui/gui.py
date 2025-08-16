from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QTabWidget,
    QWidget,
    QLabel,
    QLineEdit,
    QTextEdit,
    QPushButton,
    QFileDialog,
    QMessageBox,
    QScrollArea,
)
import sys
import os
from app.services.doc_generator import generate_jubilaciones_document


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generador de Documentos")
        self.setGeometry(300, 300, 800, 600)

        # Main layout with tabs
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Add tabs
        self.add_jubilaciones_tab()

    def add_jubilaciones_tab(self):
        # Create the Jubilaciones tab
        jubilaciones_tab = QWidget()

        # Create a scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Create a container widget for the scroll area
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        # Add input fields
        self.fields = {}

        # Add a helper function to create labeled input fields
        def add_field(label_text, placeholder_text):
            label = QLabel(label_text)
            input_field = QLineEdit()
            input_field.setPlaceholderText(placeholder_text)
            scroll_layout.addWidget(label)
            scroll_layout.addWidget(input_field)
            return input_field

        # Add all required fields
        self.fields["expediente"] = add_field("Expediente:", "Ejemplo: 32/00235-X/23")
        self.fields["departamento"] = add_field("Departamento:", "Ejemplo: OURENSE")
        self.fields["nombre"] = add_field(
            "Nombre:", "Ejemplo: MARIA TERESA COFÁN DEL RIO"
        )
        self.fields["estado_civil"] = add_field("Estado Civil:", "Ejemplo: casada")
        self.fields["dni"] = add_field("DNI:", "Ejemplo: 34597046D")
        self.fields["direccion"] = add_field(
            "Dirección:", "Ejemplo: Rua Telleira nº 8 – 4º A Ourense"
        )
        self.fields["fecha_extincion"] = add_field(
            "Fecha de Extinción:", "Ejemplo: 1 de enero de 2024"
        )
        self.fields["cobro_indebido"] = add_field(
            "Cobro Indebido:", "Ejemplo: 6.370,78 €"
        )
        self.fields["fecha_inicio"] = add_field(
            "Fecha Inicio:", "Ejemplo: enero de 2024"
        )
        self.fields["fecha_fin"] = add_field("Fecha Fin:", "Ejemplo: julio de 2025")
        self.fields["anio_1"] = add_field("Año 1:", "Ejemplo: 2024")
        self.fields["importe_indebido_anio_1"] = add_field(
            "Importe Indebido Año 1:", "Ejemplo: 7250,60 €"
        )
        self.fields["importe_mensual_anio_1"] = add_field(
            "Importe Mensual Año 1:", "Ejemplo: 517,90€"
        )
        self.fields["importe_debido_anio_1"] = add_field(
            "Importe Debido Año 1:", "Ejemplo: 5.397,42 €"
        )
        self.fields["importe_mensual_debido_anio_1"] = add_field(
            "Importe Mensual Debido Año 1:", "Ejemplo: 385,14€"
        )
        self.fields["periodo_anio_1"] = add_field(
            "Período Año 1:", "Ejemplo: 1-1-2024 a 31-12-2024"
        )
        self.fields["diferencia_anio_1"] = add_field(
            "Diferencia Año 1:", "Ejemplo: 1853,18€"
        )
        self.fields["calculo_diferencia_anio_1"] = add_field(
            "Cálculo Diferencia Año 1:", "Ejemplo: 132,37 €x14"
        )
        self.fields["anio_2"] = add_field("Año 2:", "Ejemplo: 2025")
        self.fields["nombre_esposo"] = add_field(
            "Nombre del Esposo:", "Ejemplo: Carlos Rodríguez Del Río"
        )
        self.fields["nombre_hija"] = add_field(
            "Nombre de la Hija:", "Ejemplo: Paula Del Río Cofán"
        )
        self.fields["ingresos_exponente"] = add_field(
            "Ingresos Exponente:", "Ejemplo: 0 €"
        )
        self.fields["pension_esposo_mensual"] = add_field(
            "Pensión Mensual del Esposo:", "Ejemplo: 1203 €"
        )
        self.fields["pension_esposo_anual"] = add_field(
            "Pensión Anual del Esposo:", "Ejemplo: 16.842 €"
        )
        self.fields["fecha_inicio_hija"] = add_field(
            "Fecha Inicio Hija:", "Ejemplo: 9-1-2025"
        )
        self.fields["fecha_fin_hija"] = add_field(
            "Fecha Fin Hija:", "Ejemplo: 30-6-2025"
        )
        self.fields["salarios_hija_brutos"] = add_field(
            "Salarios Brutos Hija:", "Ejemplo: 19385,72 €"
        )
        self.fields["detalle_salarios_hija"] = add_field(
            "Detalle Salarios Hija:", "Ejemplo: 2106,54 € en enero; ..."
        )
        self.fields["fecha_inicio_desempleo"] = add_field(
            "Fecha Inicio Desempleo:", "Ejemplo: 16-7-2025"
        )
        self.fields["fecha_fin_desempleo"] = add_field(
            "Fecha Fin Desempleo:", "Ejemplo: 31-12-2025"
        )
        self.fields["prestacion_desempleo"] = add_field(
            "Prestación Desempleo:", "Ejemplo: 6756,71€"
        )
        self.fields["total_ingresos"] = add_field(
            "Total Ingresos:", "Ejemplo: 42984,43 €"
        )
        self.fields["limite_ingresos"] = add_field(
            "Límite de Ingresos:", "Ejemplo: 47434,80 €/año"
        )
        self.fields["fecha_actual"] = add_field(
            "Fecha Actual:", "Ejemplo: 18 de julio de 2025"
        )
        self.fields["ciudad"] = add_field("Ciudad:", "Ejemplo: Ourense")

        # Add the Generar button
        generar_button = QPushButton("Generar")
        generar_button.clicked.connect(self.handle_generate_jubilaciones)
        scroll_layout.addWidget(generar_button)

        # Set the scroll content as the widget for the scroll area
        scroll_area.setWidget(scroll_content)

        # Set the scroll area as the layout for the Jubilaciones tab
        layout = QVBoxLayout(jubilaciones_tab)
        layout.addWidget(scroll_area)

        # Add Jubilaciones tab to main tabs
        self.tabs.addTab(jubilaciones_tab, "Jubilaciones")

    def handle_generate_jubilaciones(self):
        # Collect data from input fields
        data = {key: field.text() for key, field in self.fields.items()}

        # Validate inputs
        if not all(data.values()):
            QMessageBox.warning(self, "Error", "Por favor, completa todos los campos.")
            return

        # Open a file dialog to select where to save the document
        default_folder = os.path.join(os.path.expanduser("~"), "Documents")
        output_path, _ = QFileDialog.getSaveFileName(
            self, "Guardar archivo .docx", default_folder, "Documentos Word (*.docx)"
        )
        if not output_path:
            return

        # Call the document generation logic
        success = generate_jubilaciones_document(data, output_path)

        # Show success or error message
        if success:
            QMessageBox.information(
                self, "Éxito", f"¡Archivo generado exitosamente en:\n{output_path}!"
            )
        else:
            QMessageBox.critical(self, "Error", "Hubo un error al generar el archivo.")


# Entry point for the application
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

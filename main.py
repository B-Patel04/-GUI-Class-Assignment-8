# main.py

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from asn8_ui import Ui_root

class MainWindow(QMainWindow, Ui_root):
    def __init__(self):
        super().__init__()

        # Set up the UI
        self.setupUi(self)

        # Connect buttons to functions
        self.btnS.clicked.connect(self.submit_info)
        self.btnR.clicked.connect(self.reset_fields)
        self.btnQ.clicked.connect(self.close_application)

    # Submit button functionality
    def submit_info(self):
        first_name = self.entFirst.text().strip()
        last_name = self.entLast.text().strip()
        email = self.entEmail.text().strip()
        phone = self.entPhone.text().strip()

        # Validate first and last name
        if first_name == "" or last_name == "":
            QMessageBox.warning(
                self,
                "Input Error",
                "First Name and Last Name cannot be empty."
            )
            return

        # Print data to console
        print("First Name:", first_name)
        print("Last Name:", last_name)
        print("Email:", email)
        print("Phone:", phone)

        # Show confirmation message
        QMessageBox.information(
            self,
            "Submission Successful",
            "Information submitted successfully."
        )

    # Reset button functionality
    def reset_fields(self):
        self.entFirst.clear()
        self.entLast.clear()
        self.entEmail.clear()
        self.entPhone.clear()

    # Quit button functionality
    def close_application(self):
        self.close()


# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
import sys

import qrcode
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import *


class QrGui(QMainWindow):

    def __init__(self):
        super(QrGui, self).__init__()
        uic.loadUi('qr_main_window.ui', self)
        self.show()

        self.actionSave.triggered.connect(self.save_image)
        self.actionQuit.triggered.connect(self.quit_program)
        self.pushButton.clicked.connect(self.generate_qr_code)

    def save_image(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "PNG (*.png)",
                                                  options=options)

        if filename != "":
            img = self.label.pixmap()
            img.save(filename, "PNG")

    def generate_qr_code(self):
        qr = qrcode.QRCode(version=1,
                           error_correction=qrcode.constants.ERROR_CORRECT_L,
                           box_size=20,
                           border=2)

        qr.add_data(self.textEdit.toPlainText())
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save("QR_code.png")
        pixmap = QtGui.QPixmap("QR_code.png")
        pixmap = pixmap.scaled(400, 400)
        self.label.setPixmap(pixmap)

    @staticmethod
    def quit_program():
        sys.exit(0)


def main():
    app = QApplication([])
    _ = QrGui()
    app.exec_()


if __name__ == "__main__":
    main()

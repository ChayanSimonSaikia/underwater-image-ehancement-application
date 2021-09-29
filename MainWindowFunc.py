from PySide2 import QtWidgets, QtGui
from MainWindowUi import Ui_MainWindow


class MainWindowFunc(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # Open Image action
        self.actionOpen.triggered.connect(self.OpenAndDisplayImage)

    # Open Image Method
    def OpenAndDisplayImage(self):
        self.image_path, type = QtWidgets.QFileDialog().getOpenFileName(
            self, "Open Image", "F:\Laptop\KU Related\Major Project\Image_editor\Photos", "JPG Image Only (*.jpg)")
        self.imageMainWindowLabel.setPixmap(QtGui.QPixmap(self.image_path))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindowFunc()
    widget.show()

    app.exec_()

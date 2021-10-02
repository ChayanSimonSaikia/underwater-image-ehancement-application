from PySide2.QtCore import QRect
from Window import Window
from PySide2 import QtWidgets, QtGui


class ToolBar(Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.adjustmentBtn.clicked.connect(self.adjustmentClicked)

    def adjustmentClicked(self):
        dialog = QtWidgets.QDialog(self)

        dialog.setModal(True)
        dialog.exec()

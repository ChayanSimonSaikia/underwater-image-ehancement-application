from PySide2 import QtWidgets
from ToolBar import ToolBar
from Menu import *


class App(File, Image, Tools, Edit, ToolBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    print("Loading... Please wait")
    widget = App()
    widget.show()

    app.exec_()

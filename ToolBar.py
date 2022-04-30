from ImageInfo import ImageInfo
from Tools.tool_magicTool import MagicTool
from Window import Window
from PySide2 import QtGui
from Tools import tool_adjustment, tool_resize


class ToolBar(Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adjustment Button clicked event
        self.adjustmentBtn.clicked.connect(self.adjustmentClicked)
        self.resizeBtn.clicked.connect(self.resizeClicked)
        self.magicToolBtn.clicked.connect(self.magicToolClicked)

    # Display adjustment Window
    def adjustmentClicked(self):
        adjustment_dialog = tool_adjustment.AdjustmentTool(self)
        adjustment_dialog.setModal(True)
        adjustment_dialog.show()

    # Display resize Window
    def resizeClicked(self):
        resize_dialog = tool_resize.resizeTool(self)
        resize_dialog.setModal(True)
        resize_dialog.show()

    # Apply image enhancement
    def magicToolClicked(self):

        img = MagicTool().runMagicTool()
        try:
            img_pixmap = ImageInfo.convert_BGR2Pixmap(self, img)
            self.imageMainWindowLabel.setPixmap(
                QtGui.QPixmap(img_pixmap))
            # Update image
            ImageInfo.img_bgr = img
            ImageInfo.img_pixmap = img_pixmap
        except:
            print("Something went wrong")

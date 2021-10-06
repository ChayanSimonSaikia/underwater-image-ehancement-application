from Window import Window
from Tools import tool_adjustment, tool_resize


class ToolBar(Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adjustment Button clicked event
        self.adjustmentBtn.clicked.connect(self.adjustmentClicked)
        self.resizeBtn.clicked.connect(self.resizeClicked)

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

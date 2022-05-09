# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'v5QnUAhh.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(726, 587)
        font = QFont()
        font.setFamily(u"Nunito")
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStyleSheet(u"background-color: rgb(240, 233, 210);\n"
                                 "color: rgb(24, 29, 49);")
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockOptions(
            QMainWindow.AllowTabbedDocks | QMainWindow.AnimatedDocks)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave.setEnabled(False)
        self.actionSaveAs = QAction(MainWindow)
        self.actionSaveAs.setObjectName(u"actionSaveAs")
        self.actionSaveAs.setEnabled(False)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionImage_Size = QAction(MainWindow)
        self.actionImage_Size.setObjectName(u"actionImage_Size")
        self.actionResize_Image = QAction(MainWindow)
        self.actionResize_Image.setObjectName(u"actionResize_Image")
        self.actionClear_All_Changes = QAction(MainWindow)
        self.actionClear_All_Changes.setObjectName(u"actionClear_All_Changes")
        self.actionImageSize = QAction(MainWindow)
        self.actionImageSize.setObjectName(u"actionImageSize")
        self.actionImageSize.setEnabled(True)
        self.actionImage_Resize = QAction(MainWindow)
        self.actionImage_Resize.setObjectName(u"actionImage_Resize")
        self.actionBrightness = QAction(MainWindow)
        self.actionBrightness.setObjectName(u"actionBrightness")
        self.actionContrast = QAction(MainWindow)
        self.actionContrast.setObjectName(u"actionContrast")
        self.actionHighlight = QAction(MainWindow)
        self.actionHighlight.setObjectName(u"actionHighlight")
        self.actionShadows = QAction(MainWindow)
        self.actionShadows.setObjectName(u"actionShadows")
        self.actionCrop = QAction(MainWindow)
        self.actionCrop.setObjectName(u"actionCrop")
        self.actionHue_Saturation = QAction(MainWindow)
        self.actionHue_Saturation.setObjectName(u"actionHue_Saturation")
        self.actionLevels = QAction(MainWindow)
        self.actionLevels.setObjectName(u"actionLevels")
        self.actionDraw = QAction(MainWindow)
        self.actionDraw.setObjectName(u"actionDraw")
        self.action900176 = QAction(MainWindow)
        self.action900176.setObjectName(u"action900176")
        self.actionRotate_180 = QAction(MainWindow)
        self.actionRotate_180.setObjectName(u"actionRotate_180")
        self.actionRotate_270 = QAction(MainWindow)
        self.actionRotate_270.setObjectName(u"actionRotate_270")
        self.actionRotate_360 = QAction(MainWindow)
        self.actionRotate_360.setObjectName(u"actionRotate_360")
        self.actionFlip_Horizontally = QAction(MainWindow)
        self.actionFlip_Horizontally.setObjectName(u"actionFlip_Horizontally")
        self.actionFlip_Vertically = QAction(MainWindow)
        self.actionFlip_Vertically.setObjectName(u"actionFlip_Vertically")
        self.actionFlip_Horizontally_Vertically = QAction(MainWindow)
        self.actionFlip_Horizontally_Vertically.setObjectName(
            u"actionFlip_Horizontally_Vertically")
        self.actionAverage = QAction(MainWindow)
        self.actionAverage.setObjectName(u"actionAverage")
        self.actionGaussian_Blur = QAction(MainWindow)
        self.actionGaussian_Blur.setObjectName(u"actionGaussian_Blur")
        self.actionBillantary_Blur = QAction(MainWindow)
        self.actionBillantary_Blur.setObjectName(u"actionBillantary_Blur")
        self.actionBilateral_Blur = QAction(MainWindow)
        self.actionBilateral_Blur.setObjectName(u"actionBilateral_Blur")
        self.actionNoise_Reduction = QAction(MainWindow)
        self.actionNoise_Reduction.setObjectName(u"actionNoise_Reduction")
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionRedo_2 = QAction(MainWindow)
        self.actionRedo_2.setObjectName(u"actionRedo_2")
        self.actionClear_All = QAction(MainWindow)
        self.actionClear_All.setObjectName(u"actionClear_All")
        self.actionClear_All_Changes_2 = QAction(MainWindow)
        self.actionClear_All_Changes_2.setObjectName(
            u"actionClear_All_Changes_2")
        self.actionResize = QAction(MainWindow)
        self.actionResize.setObjectName(u"actionResize")
        self.actionRotate_90_Clockwise = QAction(MainWindow)
        self.actionRotate_90_Clockwise.setObjectName(
            u"actionRotate_90_Clockwise")
        self.actionRotate_90_Anti_Clockwise = QAction(MainWindow)
        self.actionRotate_90_Anti_Clockwise.setObjectName(
            u"actionRotate_90_Anti_Clockwise")
        self.actionBrightness_And_Contrast = QAction(MainWindow)
        self.actionBrightness_And_Contrast.setObjectName(
            u"actionBrightness_And_Contrast")
        self.actionColor_Correction = QAction(MainWindow)
        self.actionColor_Correction.setObjectName(u"actionColor_Correction")
        self.actionHue_And_Saturation = QAction(MainWindow)
        self.actionHue_And_Saturation.setObjectName(
            u"actionHue_And_Saturation")
        self.actionAuto_Image_Enhancement = QAction(MainWindow)
        self.actionAuto_Image_Enhancement.setObjectName(
            u"actionAuto_Image_Enhancement")
        self.actionNoise_Reduction_2 = QAction(MainWindow)
        self.actionNoise_Reduction_2.setObjectName(u"actionNoise_Reduction_2")
        self.actionGaussian_Blur_2 = QAction(MainWindow)
        self.actionGaussian_Blur_2.setObjectName(u"actionGaussian_Blur_2")
        self.actionUndo_2 = QAction(MainWindow)
        self.actionUndo_2.setObjectName(u"actionUndo_2")
        self.actionUndo_2.setEnabled(True)
        self.actionRedo_3 = QAction(MainWindow)
        self.actionRedo_3.setObjectName(u"actionRedo_3")
        self.actionUndo_3 = QAction(MainWindow)
        self.actionUndo_3.setObjectName(u"actionUndo_3")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ImageScrollArea = QScrollArea(self.frame)
        self.ImageScrollArea.setObjectName(u"ImageScrollArea")
        self.ImageScrollArea.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ImageScrollArea.setLayoutDirection(Qt.LeftToRight)
        self.ImageScrollArea.setFrameShape(QFrame.NoFrame)
        self.ImageScrollArea.setFrameShadow(QFrame.Plain)
        self.ImageScrollArea.setLineWidth(0)
        self.ImageScrollArea.setSizeAdjustPolicy(
            QAbstractScrollArea.AdjustIgnored)
        self.ImageScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(
            u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 634, 504))
        self.horizontalLayout_3 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.imageMainWindowLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.imageMainWindowLabel.setObjectName(u"imageMainWindowLabel")
        self.imageMainWindowLabel.setMouseTracking(True)
        self.imageMainWindowLabel.setFrameShadow(QFrame.Plain)
        self.imageMainWindowLabel.setLineWidth(0)

        self.horizontalLayout_3.addWidget(
            self.imageMainWindowLabel, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.ImageScrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_2.addWidget(self.ImageScrollArea)

        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolsPanel = QDockWidget(MainWindow)
        self.toolsPanel.setObjectName(u"toolsPanel")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.toolsPanel.sizePolicy().hasHeightForWidth())
        self.toolsPanel.setSizePolicy(sizePolicy)
        self.toolsPanel.setMinimumSize(QSize(50, 300))
        self.toolsPanel.setMaximumSize(QSize(80, 524287))
        font1 = QFont()
        font1.setFamily(u"Nunito")
        font1.setPointSize(7)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.toolsPanel.setFont(font1)
        self.toolsPanel.setCursor(QCursor(Qt.ForbiddenCursor))
        self.toolsPanel.setLayoutDirection(Qt.LeftToRight)
        self.toolsPanel.setStyleSheet(u"background-color: rgb(230, 221, 196);\n"
                                      "")
        self.toolsPanel.setInputMethodHints(Qt.ImhNone)
        self.toolsPanel.setFloating(False)
        self.toolsPanel.setFeatures(QDockWidget.DockWidgetMovable)
        self.toolsPanel.setAllowedAreas(
            Qt.BottomDockWidgetArea | Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.layoutWidget = QWidget(self.dockWidgetContents)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 31, 381))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.adjustmentBtn = QPushButton(self.layoutWidget)
        self.adjustmentBtn.setObjectName(u"adjustmentBtn")
        self.adjustmentBtn.setEnabled(False)
        self.adjustmentBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.adjustmentBtn.setMouseTracking(False)
        self.adjustmentBtn.setAcceptDrops(False)
        self.adjustmentBtn.setToolTipDuration(-1)
        self.adjustmentBtn.setStyleSheet(u"")
        self.adjustmentBtn.setInputMethodHints(Qt.ImhNone)
        icon = QIcon()
        icon.addFile(u"Icons/adjust-solid.svg",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.adjustmentBtn.setIcon(icon)
        self.adjustmentBtn.setIconSize(QSize(16, 16))
        self.adjustmentBtn.setFlat(True)

        self.verticalLayout.addWidget(self.adjustmentBtn)

        self.colorCorrectionBtn = QPushButton(self.layoutWidget)
        self.colorCorrectionBtn.setObjectName(u"colorCorrectionBtn")
        self.colorCorrectionBtn.setEnabled(False)
        self.colorCorrectionBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.colorCorrectionBtn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"Icons/sliders-h-solid.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.colorCorrectionBtn.setIcon(icon1)
        self.colorCorrectionBtn.setIconSize(QSize(16, 16))
        self.colorCorrectionBtn.setFlat(True)

        self.verticalLayout.addWidget(self.colorCorrectionBtn)

        self.HueSatBtn = QPushButton(self.layoutWidget)
        self.HueSatBtn.setObjectName(u"HueSatBtn")
        self.HueSatBtn.setEnabled(False)
        self.HueSatBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.HueSatBtn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"Icons/tint-solid.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.HueSatBtn.setIcon(icon2)
        self.HueSatBtn.setIconSize(QSize(16, 16))
        self.HueSatBtn.setFlat(True)

        self.verticalLayout.addWidget(self.HueSatBtn)

        self.magicToolBtn = QPushButton(self.layoutWidget)
        self.magicToolBtn.setObjectName(u"magicToolBtn")
        self.magicToolBtn.setEnabled(False)
        self.magicToolBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.magicToolBtn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"Icons/magic-solid.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.magicToolBtn.setIcon(icon3)
        self.magicToolBtn.setIconSize(QSize(16, 16))
        self.magicToolBtn.setFlat(True)

        self.verticalLayout.addWidget(self.magicToolBtn)

        self.resizeBtn = QPushButton(self.layoutWidget)
        self.resizeBtn.setObjectName(u"resizeBtn")
        self.resizeBtn.setEnabled(False)
        self.resizeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.resizeBtn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"Icons/compress-solid.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.resizeBtn.setIcon(icon4)
        self.resizeBtn.setIconSize(QSize(16, 16))
        self.resizeBtn.setFlat(True)

        self.verticalLayout.addWidget(self.resizeBtn)

        self.rotateBtn = QPushButton(self.layoutWidget)
        self.rotateBtn.setObjectName(u"rotateBtn")
        self.rotateBtn.setEnabled(False)
        self.rotateBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.rotateBtn.setStyleSheet(u"color: rgb(33, 50, 94);")
        icon5 = QIcon()
        icon5.addFile(u"Icons/rotate-right-solid.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.rotateBtn.setIcon(icon5)
        self.rotateBtn.setIconSize(QSize(16, 16))
        self.rotateBtn.setFlat(True)

        self.verticalLayout.addWidget(self.rotateBtn)

        self.toolsPanel.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.toolsPanel)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QRect(0, 0, 726, 25))
        self.menubar.setMinimumSize(QSize(0, 25))
        font2 = QFont()
        font2.setFamily(u"Nunito")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.menubar.setFont(font2)
        self.menubar.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.menubar.setAcceptDrops(True)
        self.menubar.setLayoutDirection(Qt.LeftToRight)
        self.menubar.setStyleSheet(
            u"selection-background-color: rgb(42, 42, 42);")
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuImage = QMenu(self.menubar)
        self.menuImage.setObjectName(u"menuImage")
        self.menuImage.setEnabled(False)
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuTools.setEnabled(False)
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuImage.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClear_All_Changes_2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuImage.addAction(self.actionUndo_3)
        self.menuImage.addSeparator()
        self.menuImage.addAction(self.actionResize)
        self.menuImage.addSeparator()
        self.menuImage.addAction(self.actionRotate_90_Clockwise)
        self.menuImage.addAction(self.actionRotate_90_Anti_Clockwise)
        self.menuTools.addAction(self.actionBrightness_And_Contrast)
        self.menuTools.addAction(self.actionColor_Correction)
        self.menuTools.addAction(self.actionHue_And_Saturation)
        self.menuTools.addAction(self.actionAuto_Image_Enhancement)
        self.menuTools.addAction(self.actionNoise_Reduction_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"Image Editor", None))
        self.actionOpen.setText(
            QCoreApplication.translate("MainWindow", u"Open", None))
# if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(
            QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(
            QCoreApplication.translate("MainWindow", u"Save", None))
# if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(
            QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSaveAs.setText(
            QCoreApplication.translate("MainWindow", u"Save As", None))
# if QT_CONFIG(shortcut)
        self.actionSaveAs.setShortcut(QCoreApplication.translate(
            "MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(
            QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionImage_Size.setText(
            QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionResize_Image.setText(
            QCoreApplication.translate("MainWindow", u"Resize Image", None))
        self.actionClear_All_Changes.setText(
            QCoreApplication.translate("MainWindow", u"Clear All Changes", None))
        self.actionImageSize.setText(QCoreApplication.translate(
            "MainWindow", u"View Resolution", None))
        self.actionImage_Resize.setText(
            QCoreApplication.translate("MainWindow", u"Resize", None))
        self.actionBrightness.setText(
            QCoreApplication.translate("MainWindow", u"Brightness", None))
        self.actionContrast.setText(
            QCoreApplication.translate("MainWindow", u"Contrast", None))
        self.actionHighlight.setText(
            QCoreApplication.translate("MainWindow", u"Highlight", None))
        self.actionShadows.setText(
            QCoreApplication.translate("MainWindow", u"Shadows", None))
        self.actionCrop.setText(
            QCoreApplication.translate("MainWindow", u"Crop", None))
        self.actionHue_Saturation.setText(QCoreApplication.translate(
            "MainWindow", u"Hue And Saturation", None))
        self.actionLevels.setText(QCoreApplication.translate(
            "MainWindow", u"Color Correction", None))
        self.actionDraw.setText(QCoreApplication.translate(
            "MainWindow", u"Add Text", None))
        self.action900176.setText(QCoreApplication.translate(
            "MainWindow", u"Rotate 90\u00b0", None))
        self.actionRotate_180.setText(QCoreApplication.translate(
            "MainWindow", u"Rotate 180\u00b0", None))
        self.actionRotate_270.setText(QCoreApplication.translate(
            "MainWindow", u"Rotate 270\u00b0", None))
        self.actionRotate_360.setText(QCoreApplication.translate(
            "MainWindow", u"Rotate 360\u00b0", None))
        self.actionFlip_Horizontally.setText(
            QCoreApplication.translate("MainWindow", u"Flip Horizontally", None))
        self.actionFlip_Vertically.setText(
            QCoreApplication.translate("MainWindow", u"Flip Vertically", None))
        self.actionFlip_Horizontally_Vertically.setText(QCoreApplication.translate(
            "MainWindow", u"Flip Horizontally + Vertically", None))
        self.actionAverage.setText(QCoreApplication.translate(
            "MainWindow", u"Average Blur", None))
        self.actionGaussian_Blur.setText(
            QCoreApplication.translate("MainWindow", u"Gaussian Blur", None))
        self.actionBillantary_Blur.setText(
            QCoreApplication.translate("MainWindow", u"Median Blur", None))
        self.actionBilateral_Blur.setText(
            QCoreApplication.translate("MainWindow", u"Bilateral Blur", None))
        self.actionNoise_Reduction.setText(
            QCoreApplication.translate("MainWindow", u"Noise Reduction", None))
        self.actionRedo.setText(
            QCoreApplication.translate("MainWindow", u"Redo", None))
        self.actionUndo.setText(
            QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionRedo_2.setText(
            QCoreApplication.translate("MainWindow", u"Redo", None))
        self.actionClear_All.setText(
            QCoreApplication.translate("MainWindow", u"Clear All", None))
        self.actionClear_All_Changes_2.setText(
            QCoreApplication.translate("MainWindow", u"Clear All Changes", None))
        self.actionResize.setText(
            QCoreApplication.translate("MainWindow", u"Resize", None))
        self.actionRotate_90_Clockwise.setText(
            QCoreApplication.translate("MainWindow", u"Rotate 90* Clockwise", None))
        self.actionRotate_90_Anti_Clockwise.setText(
            QCoreApplication.translate("MainWindow", u"Rotate 90* Anti-Clockwise", None))
        self.actionBrightness_And_Contrast.setText(
            QCoreApplication.translate("MainWindow", u"Brightness And Contrast", None))
        self.actionColor_Correction.setText(
            QCoreApplication.translate("MainWindow", u"Color Correction", None))
        self.actionHue_And_Saturation.setText(
            QCoreApplication.translate("MainWindow", u"Hue And Saturation", None))
        self.actionAuto_Image_Enhancement.setText(
            QCoreApplication.translate("MainWindow", u"Auto Image Enhancement", None))
        self.actionNoise_Reduction_2.setText(
            QCoreApplication.translate("MainWindow", u"Noise Reduction", None))
        self.actionGaussian_Blur_2.setText(
            QCoreApplication.translate("MainWindow", u"Gaussian Blur", None))
        self.actionUndo_2.setText(
            QCoreApplication.translate("MainWindow", u"Undo", None))
# if QT_CONFIG(shortcut)
        self.actionUndo_2.setShortcut(
            QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionRedo_3.setText(
            QCoreApplication.translate("MainWindow", u"Redo", None))
# if QT_CONFIG(shortcut)
        self.actionRedo_3.setShortcut(QCoreApplication.translate(
            "MainWindow", u"Ctrl+Shift+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionUndo_3.setText(
            QCoreApplication.translate("MainWindow", u"Undo", None))
# if QT_CONFIG(shortcut)
        self.actionUndo_3.setShortcut(
            QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.imageMainWindowLabel.setText("")
# if QT_CONFIG(tooltip)
        self.toolsPanel.setToolTip("")
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(whatsthis)
        self.toolsPanel.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.toolsPanel.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"ToolBar", None))
# if QT_CONFIG(tooltip)
        self.adjustmentBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Adjustment</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(statustip)
        self.adjustmentBtn.setStatusTip("")
#endif // QT_CONFIG(statustip)
# if QT_CONFIG(whatsthis)
        self.adjustmentBtn.setWhatsThis(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Adjustment Button</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
# if QT_CONFIG(accessibility)
        self.adjustmentBtn.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.adjustmentBtn.setText("")
# if QT_CONFIG(tooltip)
        self.colorCorrectionBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Color Correction</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(whatsthis)
        self.colorCorrectionBtn.setWhatsThis(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Color Correction Button</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.colorCorrectionBtn.setText("")
# if QT_CONFIG(tooltip)
        self.HueSatBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Hue And Saturation</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(whatsthis)
        self.HueSatBtn.setWhatsThis(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Hue and Saturation button</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.HueSatBtn.setText("")
# if QT_CONFIG(tooltip)
        self.magicToolBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Magic Tools</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(whatsthis)
        self.magicToolBtn.setWhatsThis(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Magic tool Button</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.magicToolBtn.setText("")
# if QT_CONFIG(tooltip)
        self.resizeBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Resize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(whatsthis)
        self.resizeBtn.setWhatsThis(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Resize Image</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.resizeBtn.setText("")
# if QT_CONFIG(tooltip)
        self.rotateBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Resize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(whatsthis)
        self.rotateBtn.setWhatsThis(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Resize Image</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.rotateBtn.setText("")
        self.menuFile.setTitle(
            QCoreApplication.translate("MainWindow", u"File", None))
        self.menuImage.setTitle(
            QCoreApplication.translate("MainWindow", u"Image", None))
        self.menuTools.setTitle(
            QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

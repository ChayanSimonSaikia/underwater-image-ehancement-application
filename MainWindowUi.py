# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'v3qmTsRk.ui'
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
        MainWindow.resize(722, 600)
        font = QFont()
        font.setFamily(u"Nunito")
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStyleSheet(u"background-color: rgb(46, 46, 58);\n"
                                 "color: rgb(224, 224, 224);")
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 630, 517))
        self.horizontalLayout_3 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.imageMainWindowLabel = QLabel(self.scrollAreaWidgetContents_2)
        # self.imageMainWindowLabel.setScaledContents(True)
        # self.imageMainWindowLabel.setSizePolicy(
        #     QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageMainWindowLabel.setObjectName(u"imageMainWindowLabel")
        self.imageMainWindowLabel.setMouseTracking(True)
        self.imageMainWindowLabel.setFrameShadow(QFrame.Plain)
        self.imageMainWindowLabel.setLineWidth(0)

        self.horizontalLayout_3.addWidget(
            self.imageMainWindowLabel, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.ImageScrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_2.addWidget(self.ImageScrollArea)

        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QRect(0, 0, 722, 25))
        self.menubar.setMinimumSize(QSize(0, 25))
        font1 = QFont()
        font1.setFamily(u"Nunito")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.menubar.setFont(font1)
        self.menubar.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.menubar.setAcceptDrops(True)
        self.menubar.setLayoutDirection(Qt.LeftToRight)
        self.menubar.setStyleSheet(
            u"selection-background-color: rgb(42, 42, 42);")
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuImage_2 = QMenu(self.menubar)
        self.menuImage_2.setObjectName(u"menuImage_2")
        self.menuImage_2.setEnabled(False)
        self.menuRotate = QMenu(self.menuImage_2)
        self.menuRotate.setObjectName(u"menuRotate")
        self.menuFlip = QMenu(self.menuImage_2)
        self.menuFlip.setObjectName(u"menuFlip")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuTools.setEnabled(False)
        self.menuAdjustments = QMenu(self.menuTools)
        self.menuAdjustments.setObjectName(u"menuAdjustments")
        self.menuBlur = QMenu(self.menuTools)
        self.menuBlur.setObjectName(u"menuBlur")
        MainWindow.setMenuBar(self.menubar)
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
        font2 = QFont()
        font2.setFamily(u"Nunito")
        font2.setPointSize(7)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(75)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.toolsPanel.setFont(font2)
        self.toolsPanel.setCursor(QCursor(Qt.ForbiddenCursor))
        self.toolsPanel.setLayoutDirection(Qt.LeftToRight)
        self.toolsPanel.setStyleSheet(u"background-color: rgb(60, 60, 75);")
        self.toolsPanel.setInputMethodHints(Qt.ImhNone)
        self.toolsPanel.setFloating(False)
        self.toolsPanel.setFeatures(QDockWidget.DockWidgetMovable)
        self.toolsPanel.setAllowedAreas(
            Qt.BottomDockWidgetArea | Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayoutWidget = QWidget(self.dockWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 30, 291))
        self.verticalLayout = QVBoxLayout(self.gridLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TextBtn = QPushButton(self.gridLayoutWidget)
        self.TextBtn.setObjectName(u"TextBtn")
        self.TextBtn.setEnabled(False)
        self.TextBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.TextBtn.setStyleSheet(u"selection-color: rgb(28, 28, 28);\n"
                                   "color: rgb(28, 28, 28);")
        icon = QIcon()
        icon.addFile(u"../Image_editor/Icons/font-solid.svg",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.TextBtn.setIcon(icon)
        self.TextBtn.setIconSize(QSize(14, 14))
        self.TextBtn.setFlat(True)

        self.verticalLayout.addWidget(self.TextBtn)

        self.adjustmentBtn = QPushButton(self.gridLayoutWidget)
        self.adjustmentBtn.setObjectName(u"adjustmentBtn")
        self.adjustmentBtn.setEnabled(False)
        self.adjustmentBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.adjustmentBtn.setMouseTracking(False)
        self.adjustmentBtn.setAcceptDrops(False)
        self.adjustmentBtn.setToolTipDuration(-1)
        self.adjustmentBtn.setStyleSheet(u"selection-color: rgb(28, 28, 28);\n"
                                         "color: rgb(28, 28, 28);")
        self.adjustmentBtn.setInputMethodHints(Qt.ImhNone)
        icon1 = QIcon()
        icon1.addFile(u"../Image_editor/Icons/adjust-solid.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.adjustmentBtn.setIcon(icon1)
        self.adjustmentBtn.setIconSize(QSize(14, 14))
        self.adjustmentBtn.setFlat(True)

        self.verticalLayout.addWidget(self.adjustmentBtn)

        self.colorCorrectionBtn = QPushButton(self.gridLayoutWidget)
        self.colorCorrectionBtn.setObjectName(u"colorCorrectionBtn")
        self.colorCorrectionBtn.setEnabled(False)
        self.colorCorrectionBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.colorCorrectionBtn.setStyleSheet(u"selection-color: rgb(28, 28, 28);\n"
                                              "color: rgb(28, 28, 28);")
        icon2 = QIcon()
        icon2.addFile(u"../Image_editor/Icons/sliders-h-solid.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.colorCorrectionBtn.setIcon(icon2)
        self.colorCorrectionBtn.setIconSize(QSize(14, 14))
        self.colorCorrectionBtn.setFlat(True)

        self.verticalLayout.addWidget(self.colorCorrectionBtn)

        self.HueSatBtn = QPushButton(self.gridLayoutWidget)
        self.HueSatBtn.setObjectName(u"HueSatBtn")
        self.HueSatBtn.setEnabled(False)
        self.HueSatBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.HueSatBtn.setStyleSheet(u"selection-color: rgb(28, 28, 28);\n"
                                     "color: rgb(28, 28, 28);")
        icon3 = QIcon()
        icon3.addFile(u"../Image_editor/Icons/tint-solid.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.HueSatBtn.setIcon(icon3)
        self.HueSatBtn.setIconSize(QSize(14, 14))
        self.HueSatBtn.setFlat(True)

        self.verticalLayout.addWidget(self.HueSatBtn)

        self.magicToolBtn = QPushButton(self.gridLayoutWidget)
        self.magicToolBtn.setObjectName(u"magicToolBtn")
        self.magicToolBtn.setEnabled(False)
        self.magicToolBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.magicToolBtn.setStyleSheet(u"selection-color: rgb(28, 28, 28);\n"
                                        "color: rgb(28, 28, 28);")
        icon4 = QIcon()
        icon4.addFile(u"../Image_editor/Icons/magic-solid.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.magicToolBtn.setIcon(icon4)
        self.magicToolBtn.setIconSize(QSize(14, 14))
        self.magicToolBtn.setFlat(True)

        self.verticalLayout.addWidget(self.magicToolBtn)

        self.cropBtn = QPushButton(self.gridLayoutWidget)
        self.cropBtn.setObjectName(u"cropBtn")
        self.cropBtn.setEnabled(False)
        self.cropBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cropBtn.setStyleSheet(u"selection-color: rgb(28, 28, 28);\n"
                                   "color: rgb(28, 28, 28);")
        icon5 = QIcon()
        icon5.addFile(u"../Image_editor/Icons/crop-alt-solid.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.cropBtn.setIcon(icon5)
        self.cropBtn.setIconSize(QSize(14, 14))
        self.cropBtn.setFlat(True)

        self.verticalLayout.addWidget(self.cropBtn)

        self.colorPickerBtn = QPushButton(self.gridLayoutWidget)
        self.colorPickerBtn.setObjectName(u"colorPickerBtn")
        self.colorPickerBtn.setEnabled(False)
        self.colorPickerBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.colorPickerBtn.setStyleSheet(u"selection-color: rgb(28, 28, 28);\n"
                                          "color: rgb(28, 28, 28);")
        icon6 = QIcon()
        icon6.addFile(u"../Image_editor/Icons/palette-solid.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.colorPickerBtn.setIcon(icon6)
        self.colorPickerBtn.setIconSize(QSize(14, 14))
        self.colorPickerBtn.setFlat(True)

        self.verticalLayout.addWidget(self.colorPickerBtn)

        self.resizeBtn = QPushButton(self.gridLayoutWidget)
        self.resizeBtn.setObjectName(u"resizeBtn")
        self.resizeBtn.setEnabled(False)
        self.resizeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.resizeBtn.setStyleSheet(u"selection-color: rgb(28, 28, 28);\n"
                                     "color: rgb(28, 28, 28);")
        icon7 = QIcon()
        icon7.addFile(u"../Image_editor/Icons/compress-solid.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.resizeBtn.setIcon(icon7)
        self.resizeBtn.setIconSize(QSize(14, 14))
        self.resizeBtn.setFlat(True)

        self.verticalLayout.addWidget(self.resizeBtn)

        self.TextBtn.raise_()
        self.colorCorrectionBtn.raise_()
        self.HueSatBtn.raise_()
        self.cropBtn.raise_()
        self.magicToolBtn.raise_()
        self.resizeBtn.raise_()
        self.colorPickerBtn.raise_()
        self.adjustmentBtn.raise_()
        self.toolsPanel.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.toolsPanel)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuImage_2.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClear_All_Changes_2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuImage_2.addAction(self.actionImageSize)
        self.menuImage_2.addAction(self.actionImage_Resize)
        self.menuImage_2.addSeparator()
        self.menuImage_2.addAction(self.actionCrop)
        self.menuImage_2.addSeparator()
        self.menuImage_2.addAction(self.menuRotate.menuAction())
        self.menuImage_2.addAction(self.menuFlip.menuAction())
        self.menuRotate.addAction(self.action900176)
        self.menuRotate.addAction(self.actionRotate_180)
        self.menuRotate.addAction(self.actionRotate_270)
        self.menuRotate.addAction(self.actionRotate_360)
        self.menuFlip.addAction(self.actionFlip_Horizontally)
        self.menuFlip.addAction(self.actionFlip_Vertically)
        self.menuTools.addAction(self.menuAdjustments.menuAction())
        self.menuTools.addAction(self.actionHue_Saturation)
        self.menuTools.addAction(self.actionLevels)
        self.menuTools.addAction(self.actionDraw)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.menuBlur.menuAction())
        self.menuTools.addAction(self.actionNoise_Reduction)
        self.menuAdjustments.addAction(self.actionBrightness)
        self.menuAdjustments.addAction(self.actionContrast)
        self.menuAdjustments.addAction(self.actionHighlight)
        self.menuAdjustments.addAction(self.actionShadows)
        self.menuBlur.addAction(self.actionAverage)
        self.menuBlur.addAction(self.actionGaussian_Blur)
        self.menuBlur.addAction(self.actionBillantary_Blur)
        self.menuBlur.addAction(self.actionBilateral_Blur)

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
        self.imageMainWindowLabel.setText("")
        self.menuFile.setTitle(
            QCoreApplication.translate("MainWindow", u"File", None))
        self.menuImage_2.setTitle(
            QCoreApplication.translate("MainWindow", u"Image", None))
        self.menuRotate.setTitle(
            QCoreApplication.translate("MainWindow", u"Rotate", None))
        self.menuFlip.setTitle(
            QCoreApplication.translate("MainWindow", u"Flip", None))
        self.menuTools.setTitle(
            QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuAdjustments.setTitle(
            QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.menuBlur.setTitle(
            QCoreApplication.translate("MainWindow", u"Blur", None))
# if QT_CONFIG(tooltip)
        self.toolsPanel.setToolTip("")
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(whatsthis)
        self.toolsPanel.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.toolsPanel.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"ToolBar", None))
# if QT_CONFIG(tooltip)
        self.TextBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Text</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(whatsthis)
        self.TextBtn.setWhatsThis(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Add text Button</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.TextBtn.setText("")
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
        self.cropBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Crop</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(whatsthis)
        self.cropBtn.setWhatsThis(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Crop Button</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.cropBtn.setText("")
# if QT_CONFIG(tooltip)
        self.colorPickerBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Color Picker</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(whatsthis)
        self.colorPickerBtn.setWhatsThis(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Color Picker Button</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.colorPickerBtn.setText("")
# if QT_CONFIG(tooltip)
        self.resizeBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Resize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(whatsthis)
        self.resizeBtn.setWhatsThis(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p>Resize Image</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.resizeBtn.setText("")
    # retranslateUi

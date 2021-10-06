# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'resizeDialogwNBhAt.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Resize(object):
    def setupUi(self, Resize):
        if not Resize.objectName():
            Resize.setObjectName(u"Resize")
        Resize.resize(262, 300)
        icon = QIcon()
        icon.addFile(u"../Image_editor/Icons/compress-solid.svg",
                     QSize(), QIcon.Normal, QIcon.Off)
        Resize.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(Resize)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(Resize)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.lockCheck_2 = QCheckBox(self.frame_3)
        self.lockCheck_2.setObjectName(u"lockCheck_2")
        self.lockCheck_2.setGeometry(QRect(10, 10, 70, 17))

        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame = QFrame(Resize)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.widthVal = QSpinBox(self.frame)
        self.widthVal.setObjectName(u"widthVal")
        self.widthVal.setAlignment(Qt.AlignCenter)
        self.widthVal.setMinimum(0)
        self.widthVal.setMaximum(10000)

        self.horizontalLayout_2.addWidget(self.widthVal)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.heightVal = QSpinBox(self.frame)
        self.heightVal.setObjectName(u"heightVal")
        self.heightVal.setAlignment(Qt.AlignCenter)
        self.heightVal.setMinimum(0)
        self.heightVal.setMaximum(10000)

        self.horizontalLayout.addWidget(self.heightVal)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(Resize)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.cancelBtn = QPushButton(self.frame_2)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout_3.addWidget(self.cancelBtn, 0, Qt.AlignBottom)

        self.okBtn = QPushButton(self.frame_2)
        self.okBtn.setObjectName(u"okBtn")

        self.horizontalLayout_3.addWidget(self.okBtn, 0, Qt.AlignBottom)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.retranslateUi(Resize)

        QMetaObject.connectSlotsByName(Resize)
    # setupUi

    def retranslateUi(self, Resize):
        Resize.setWindowTitle(
            QCoreApplication.translate("Resize", u"Resize", None))
        self.lockCheck_2.setText(
            QCoreApplication.translate("Resize", u"Lock", None))
        self.label.setText(QCoreApplication.translate(
            "Resize", u"Width", None))
        self.label_3.setText(
            QCoreApplication.translate("Resize", u"Pixels", None))
        self.label_2.setText(
            QCoreApplication.translate("Resize", u"Height", None))
        self.label_4.setText(
            QCoreApplication.translate("Resize", u"Pixels", None))
        self.okBtn.setText(QCoreApplication.translate("Resize", u"OK", None))
        self.cancelBtn.setText(
            QCoreApplication.translate("Resize", u"Cancel", None))
    # retranslateUi

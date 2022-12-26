# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'miui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Georgia"])
        Form.setFont(font)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 0, 791, 173))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setMinimumSize(QSize(14, 50))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        self.pushButton.setFont(font1)

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setMinimumSize(QSize(14, 50))
        self.pushButton_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.pushButton_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        font2 = QFont()
        font2.setFamilies([u"Georgia"])
        font2.setPointSize(26)
        font2.setBold(True)
        font2.setItalic(False)
        self.label_2.setFont(font2)
        self.label_2.setToolTipDuration(0)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(17, 190, 774, 121))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setFamilies([u"Georgia"])
        font3.setPointSize(14)
        self.label_4.setFont(font3)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 320, 123, 281))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(50, 60))

        self.verticalLayout_4.addWidget(self.pushButton_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.verticalSlider = QSlider(self.widget)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_4.addWidget(self.verticalSlider)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Open connection", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Close connection", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Device is not defined", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"1. Push a button or drag a fader that needs to be checked. \n"
"2. Push \"Take selection\" or reset if mistaken.\n"
"3. Wait 3 seconds until the message pops.", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Note name will be showed here...", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi


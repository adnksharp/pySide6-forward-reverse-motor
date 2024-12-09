# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLCDNumber, QLabel, QPushButton, QSizePolicy,
    QSlider, QSpinBox, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(182, 350)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_4 = QGroupBox(Widget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lcdNumber = QLCDNumber(self.groupBox_4)
        self.lcdNumber.setObjectName(u"lcdNumber")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setFrameShape(QFrame.Shape.NoFrame)
        self.lcdNumber.setFrameShadow(QFrame.Shadow.Plain)
        self.lcdNumber.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.horizontalLayout.addWidget(self.lcdNumber)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pwmSlider = QSlider(self.groupBox_2)
        self.pwmSlider.setObjectName(u"pwmSlider")
        self.pwmSlider.setMaximum(100)
        self.pwmSlider.setValue(100)
        self.pwmSlider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_2.addWidget(self.pwmSlider)

        self.pwmSpin = QSpinBox(self.groupBox_2)
        self.pwmSpin.setObjectName(u"pwmSpin")
        self.pwmSpin.setFrame(False)
        self.pwmSpin.setMaximum(100)
        self.pwmSpin.setValue(100)

        self.horizontalLayout_2.addWidget(self.pwmSpin)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.drive = QPushButton(self.groupBox)
        self.drive.setObjectName(u"drive")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.drive.sizePolicy().hasHeightForWidth())
        self.drive.setSizePolicy(sizePolicy2)
        self.drive.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.drive.setStyleSheet(u"color: #59ff00;\n"
"background-color: black;")
        self.drive.setAutoDefault(False)
        self.drive.setFlat(False)

        self.verticalLayout.addWidget(self.drive)

        self.reverse = QPushButton(self.groupBox)
        self.reverse.setObjectName(u"reverse")
        sizePolicy2.setHeightForWidth(self.reverse.sizePolicy().hasHeightForWidth())
        self.reverse.setSizePolicy(sizePolicy2)
        self.reverse.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.reverse.setStyleSheet(u"color: #00b3ff;\n"
"background-color: black;")
        self.reverse.setAutoDefault(False)
        self.reverse.setFlat(False)

        self.verticalLayout.addWidget(self.reverse)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(Widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy3)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stop = QPushButton(self.groupBox_3)
        self.stop.setObjectName(u"stop")
        sizePolicy2.setHeightForWidth(self.stop.sizePolicy().hasHeightForWidth())
        self.stop.setSizePolicy(sizePolicy2)
        self.stop.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.stop.setStyleSheet(u"color: #ff2457;\n"
"background-color: black;")
        self.stop.setAutoDefault(False)
        self.stop.setFlat(False)

        self.verticalLayout_3.addWidget(self.stop)


        self.verticalLayout_2.addWidget(self.groupBox_3)


        self.retranslateUi(Widget)

        self.drive.setDefault(False)
        self.reverse.setDefault(False)
        self.stop.setDefault(False)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Motor", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Widget", u"SALIDA", None))
        self.label.setText(QCoreApplication.translate("Widget", u"V", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"VELOCIDAD", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"ARRANQUE", None))
        self.drive.setText(QCoreApplication.translate("Widget", u"DIRECTO", None))
        self.reverse.setText(QCoreApplication.translate("Widget", u"REVERSA", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"PARO", None))
        self.stop.setText(QCoreApplication.translate("Widget", u"APAGAR", None))
    # retranslateUi


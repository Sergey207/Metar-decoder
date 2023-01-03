# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QAbstractItemView, QComboBox, QHBoxLayout,
                               QLabel, QLineEdit, QListWidget,
                               QPushButton, QSizePolicy,
                               QSpacerItem, QTableWidget, QVBoxLayout,
                               QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblAirportCode = QLabel(self.centralwidget)
        self.lblAirportCode.setObjectName(u"lblAirportCode")

        self.horizontalLayout.addWidget(self.lblAirportCode)

        self.edtAirportCode = QLineEdit(self.centralwidget)
        self.edtAirportCode.setObjectName(u"edtAirportCode")

        self.horizontalLayout.addWidget(self.edtAirportCode)

        self.btnAddToQuickbar = QPushButton(self.centralwidget)
        self.btnAddToQuickbar.setObjectName(u"btnAddToQuickbar")
        self.btnAddToQuickbar.setMinimumSize(QSize(24, 24))
        self.btnAddToQuickbar.setMaximumSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btnAddToQuickbar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lstQuickbar = QListWidget(self.centralwidget)
        self.lstQuickbar.setObjectName(u"lstQuickbar")
        self.lstQuickbar.setMaximumSize(QSize(75, 16777215))

        self.verticalLayout_5.addWidget(self.lstQuickbar)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tblResult = QTableWidget(self.centralwidget)
        self.tblResult.setObjectName(u"tblResult")
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tblResult.setSelectionMode(QAbstractItemView.NoSelection)
        self.tblResult.setTextElideMode(Qt.ElideNone)
        self.tblResult.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tblResult.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tblResult.setGridStyle(Qt.SolidLine)
        self.tblResult.verticalHeader().setVisible(False)

        self.horizontalLayout_5.addWidget(self.tblResult)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lblArrow = QLabel(self.centralwidget)
        self.lblArrow.setObjectName(u"lblArrow")
        self.lblArrow.setMinimumSize(QSize(180, 180))
        self.lblArrow.setMaximumSize(QSize(180, 180))

        self.verticalLayout_2.addWidget(self.lblArrow)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_14.addWidget(self.label_7)

        self.edtNM = QLineEdit(self.centralwidget)
        self.edtNM.setObjectName(u"edtNM")

        self.horizontalLayout_14.addWidget(self.edtNM)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 4)

        self.verticalLayout_2.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_12.addWidget(self.label_5)

        self.edtM = QLineEdit(self.centralwidget)
        self.edtM.setObjectName(u"edtM")

        self.horizontalLayout_12.addWidget(self.edtM)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 4)

        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_13.addWidget(self.label_6)

        self.edtKM = QLineEdit(self.centralwidget)
        self.edtKM.setObjectName(u"edtKM")

        self.horizontalLayout_13.addWidget(self.edtKM)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 4)

        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.edtHPA = QLineEdit(self.centralwidget)
        self.edtHPA.setObjectName(u"edtHPA")

        self.horizontalLayout_4.addWidget(self.edtHPA)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 4)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.edtMMRT = QLineEdit(self.centralwidget)
        self.edtMMRT.setObjectName(u"edtMMRT")

        self.horizontalLayout_2.addWidget(self.edtMMRT)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.edtENCHRT = QLineEdit(self.centralwidget)
        self.edtENCHRT.setObjectName(u"edtENCHRT")

        self.horizontalLayout_3.addWidget(self.edtENCHRT)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 4)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.horizontalLayout_5.setStretch(0, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.edtMetarCode = QLineEdit(self.centralwidget)
        self.edtMetarCode.setObjectName(u"edtMetarCode")
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(True)
        self.edtMetarCode.setFont(font1)
        self.edtMetarCode.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.edtMetarCode)

        self.cmbLanguage = QComboBox(self.centralwidget)
        self.cmbLanguage.setObjectName(u"cmbLanguage")

        self.horizontalLayout_15.addWidget(self.cmbLanguage)


        self.verticalLayout_4.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Metar Decoder", None))
        self.lblAirportCode.setText(QCoreApplication.translate("MainWindow", u"Airport code:", None))
        self.btnAddToQuickbar.setText("")
        self.lblArrow.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"NM", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"KM", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"HPA", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MM", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"INCH", None))
    # retranslateUi


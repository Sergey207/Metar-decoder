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
from PySide6.QtWidgets import (QAbstractItemView, QButtonGroup, QComboBox,
                               QGridLayout, QHBoxLayout, QLabel,
                               QLayout, QLineEdit, QListWidget, QPushButton, QSizePolicy, QSpacerItem,
                               QTabWidget, QTableWidget, QVBoxLayout,
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
        self.horizontalLayout_9 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabMetar = QWidget()
        self.tabMetar.setObjectName(u"tabMetar")
        self.verticalLayout_4 = QVBoxLayout(self.tabMetar)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblAirportCode = QLabel(self.tabMetar)
        self.lblAirportCode.setObjectName(u"lblAirportCode")

        self.horizontalLayout.addWidget(self.lblAirportCode)

        self.edtAirportCode = QLineEdit(self.tabMetar)
        self.edtAirportCode.setObjectName(u"edtAirportCode")

        self.horizontalLayout.addWidget(self.edtAirportCode)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lytQuickBar = QVBoxLayout()
        self.lytQuickBar.setObjectName(u"lytQuickBar")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.lytQuickBar.addItem(self.verticalSpacer_3)


        self.horizontalLayout_12.addLayout(self.lytQuickBar)

        self.tblResult = QTableWidget(self.tabMetar)
        self.tblResult.setObjectName(u"tblResult")
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tblResult.setSelectionMode(QAbstractItemView.NoSelection)
        self.tblResult.setTextElideMode(Qt.ElideNone)
        self.tblResult.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tblResult.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tblResult.setGridStyle(Qt.SolidLine)
        self.tblResult.verticalHeader().setVisible(False)

        self.horizontalLayout_12.addWidget(self.tblResult)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lblArrow = QLabel(self.tabMetar)
        self.lblArrow.setObjectName(u"lblArrow")
        self.lblArrow.setMinimumSize(QSize(180, 180))
        self.lblArrow.setMaximumSize(QSize(180, 180))

        self.horizontalLayout_5.addWidget(self.lblArrow)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.tabMetar)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.edtHPA = QLineEdit(self.tabMetar)
        self.edtHPA.setObjectName(u"edtHPA")

        self.horizontalLayout_4.addWidget(self.edtHPA)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 4)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.tabMetar)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.edtMMRT = QLineEdit(self.tabMetar)
        self.edtMMRT.setObjectName(u"edtMMRT")

        self.horizontalLayout_2.addWidget(self.edtMMRT)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.tabMetar)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.edtENCHRT = QLineEdit(self.tabMetar)
        self.edtENCHRT.setObjectName(u"edtENCHRT")

        self.horizontalLayout_3.addWidget(self.edtENCHRT)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 4)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_12.addLayout(self.verticalLayout_2)

        self.horizontalLayout_12.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.edtMetarCode = QLineEdit(self.tabMetar)
        self.edtMetarCode.setObjectName(u"edtMetarCode")
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setItalic(True)
        self.edtMetarCode.setFont(font1)
        self.edtMetarCode.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.edtMetarCode)

        self.tabWidget.addTab(self.tabMetar, "")
        self.tabSettings = QWidget()
        self.tabSettings.setObjectName(u"tabSettings")
        self.horizontalLayout_11 = QHBoxLayout(self.tabSettings)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lblLanguage = QLabel(self.tabSettings)
        self.lblLanguage.setObjectName(u"lblLanguage")

        self.horizontalLayout_6.addWidget(self.lblLanguage)

        self.cmbLanguage = QComboBox(self.tabSettings)
        self.cmbLanguage.setObjectName(u"cmbLanguage")

        self.horizontalLayout_6.addWidget(self.cmbLanguage)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lblQuickbar = QLabel(self.tabSettings)
        self.lblQuickbar.setObjectName(u"lblQuickbar")

        self.horizontalLayout_8.addWidget(self.lblQuickbar)

        self.lstQuickBar = QListWidget(self.tabSettings)
        self.lstQuickBar.setObjectName(u"lstQuickBar")

        self.horizontalLayout_8.addWidget(self.lstQuickBar)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.btnQuickbarMinus = QPushButton(self.tabSettings)
        self.btnQuickbarMinus.setObjectName(u"btnQuickbarMinus")
        self.btnQuickbarMinus.setMinimumSize(QSize(27, 27))
        self.btnQuickbarMinus.setMaximumSize(QSize(27, 27))

        self.horizontalLayout_10.addWidget(self.btnQuickbarMinus)

        self.btnQuickbarPlus = QPushButton(self.tabSettings)
        self.btnQuickbarPlus.setObjectName(u"btnQuickbarPlus")
        self.btnQuickbarPlus.setMinimumSize(QSize(27, 27))
        self.btnQuickbarPlus.setMaximumSize(QSize(27, 27))

        self.horizontalLayout_10.addWidget(self.btnQuickbarPlus)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btnSaveSettings = QPushButton(self.tabSettings)
        self.btnSaveSettings.setObjectName(u"btnSaveSettings")

        self.horizontalLayout_7.addWidget(self.btnSaveSettings)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_11.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.edtExpression = QLineEdit(self.tabSettings)
        self.edtExpression.setObjectName(u"edtExpression")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtExpression.sizePolicy().hasHeightForWidth())
        self.edtExpression.setSizePolicy(sizePolicy)
        self.edtExpression.setReadOnly(False)

        self.verticalLayout_3.addWidget(self.edtExpression)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.btnLS = QPushButton(self.tabSettings)
        self.grpActions = QButtonGroup(MainWindow)
        self.grpActions.setObjectName(u"grpActions")
        self.grpActions.addButton(self.btnLS)
        self.btnLS.setObjectName(u"btnLS")
        self.btnLS.setMinimumSize(QSize(50, 50))
        self.btnLS.setMaximumSize(QSize(50, 50))
        font2 = QFont()
        font2.setFamilies([u"Calibri"])
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setItalic(True)
        self.btnLS.setFont(font2)

        self.gridLayout.addWidget(self.btnLS, 0, 0, 1, 1)

        self.btnDel = QPushButton(self.tabSettings)
        self.grpActions.addButton(self.btnDel)
        self.btnDel.setObjectName(u"btnDel")
        self.btnDel.setMinimumSize(QSize(50, 50))
        self.btnDel.setMaximumSize(QSize(50, 50))
        self.btnDel.setFont(font2)

        self.gridLayout.addWidget(self.btnDel, 3, 3, 1, 1)

        self.btnPlus = QPushButton(self.tabSettings)
        self.grpActions.addButton(self.btnPlus)
        self.btnPlus.setObjectName(u"btnPlus")
        self.btnPlus.setMinimumSize(QSize(50, 50))
        self.btnPlus.setMaximumSize(QSize(50, 50))
        self.btnPlus.setFont(font2)

        self.gridLayout.addWidget(self.btnPlus, 0, 3, 1, 1)

        self.btn2 = QPushButton(self.tabSettings)
        self.grpDigits = QButtonGroup(MainWindow)
        self.grpDigits.setObjectName(u"grpDigits")
        self.grpDigits.addButton(self.btn2)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setMinimumSize(QSize(50, 50))
        self.btn2.setMaximumSize(QSize(50, 50))
        self.btn2.setFont(font2)

        self.gridLayout.addWidget(self.btn2, 1, 1, 1, 1)

        self.btn3 = QPushButton(self.tabSettings)
        self.grpDigits.addButton(self.btn3)
        self.btn3.setObjectName(u"btn3")
        self.btn3.setMinimumSize(QSize(50, 50))
        self.btn3.setMaximumSize(QSize(50, 50))
        self.btn3.setFont(font2)

        self.gridLayout.addWidget(self.btn3, 1, 2, 1, 1)

        self.btn0 = QPushButton(self.tabSettings)
        self.grpDigits.addButton(self.btn0)
        self.btn0.setObjectName(u"btn0")
        self.btn0.setMinimumSize(QSize(50, 50))
        self.btn0.setMaximumSize(QSize(50, 50))
        self.btn0.setFont(font2)

        self.gridLayout.addWidget(self.btn0, 4, 0, 1, 1)

        self.btn7 = QPushButton(self.tabSettings)
        self.grpDigits.addButton(self.btn7)
        self.btn7.setObjectName(u"btn7")
        self.btn7.setMinimumSize(QSize(50, 50))
        self.btn7.setMaximumSize(QSize(50, 50))
        self.btn7.setBaseSize(QSize(50, 50))
        self.btn7.setFont(font2)

        self.gridLayout.addWidget(self.btn7, 3, 0, 1, 1)

        self.btnStepen = QPushButton(self.tabSettings)
        self.grpActions.addButton(self.btnStepen)
        self.btnStepen.setObjectName(u"btnStepen")
        self.btnStepen.setMinimumSize(QSize(50, 50))
        self.btnStepen.setMaximumSize(QSize(50, 50))
        self.btnStepen.setFont(font2)

        self.gridLayout.addWidget(self.btnStepen, 0, 2, 1, 1)

        self.btnUmno = QPushButton(self.tabSettings)
        self.grpActions.addButton(self.btnUmno)
        self.btnUmno.setObjectName(u"btnUmno")
        self.btnUmno.setMinimumSize(QSize(50, 50))
        self.btnUmno.setMaximumSize(QSize(50, 50))
        self.btnUmno.setFont(font2)

        self.gridLayout.addWidget(self.btnUmno, 2, 3, 1, 1)

        self.btn8 = QPushButton(self.tabSettings)
        self.grpDigits.addButton(self.btn8)
        self.btn8.setObjectName(u"btn8")
        self.btn8.setMinimumSize(QSize(50, 50))
        self.btn8.setMaximumSize(QSize(50, 50))
        self.btn8.setFont(font2)

        self.gridLayout.addWidget(self.btn8, 3, 1, 1, 1)

        self.btn5 = QPushButton(self.tabSettings)
        self.grpDigits.addButton(self.btn5)
        self.btn5.setObjectName(u"btn5")
        self.btn5.setMinimumSize(QSize(50, 50))
        self.btn5.setMaximumSize(QSize(50, 50))
        self.btn5.setFont(font2)

        self.gridLayout.addWidget(self.btn5, 2, 1, 1, 1)

        self.btn4 = QPushButton(self.tabSettings)
        self.grpDigits.addButton(self.btn4)
        self.btn4.setObjectName(u"btn4")
        self.btn4.setMinimumSize(QSize(50, 50))
        self.btn4.setMaximumSize(QSize(50, 50))
        self.btn4.setFont(font2)

        self.gridLayout.addWidget(self.btn4, 2, 0, 1, 1)

        self.btnMinus = QPushButton(self.tabSettings)
        self.grpActions.addButton(self.btnMinus)
        self.btnMinus.setObjectName(u"btnMinus")
        self.btnMinus.setMinimumSize(QSize(50, 50))
        self.btnMinus.setMaximumSize(QSize(50, 50))
        self.btnMinus.setFont(font2)

        self.gridLayout.addWidget(self.btnMinus, 1, 3, 1, 1)

        self.btnRes = QPushButton(self.tabSettings)
        self.grpActions.addButton(self.btnRes)
        self.btnRes.setObjectName(u"btnRes")
        self.btnRes.setMinimumSize(QSize(50, 50))
        self.btnRes.setMaximumSize(QSize(50, 50))
        self.btnRes.setFont(font2)

        self.gridLayout.addWidget(self.btnRes, 4, 3, 1, 1)

        self.btn9 = QPushButton(self.tabSettings)
        self.grpDigits.addButton(self.btn9)
        self.btn9.setObjectName(u"btn9")
        self.btn9.setMinimumSize(QSize(50, 50))
        self.btn9.setMaximumSize(QSize(50, 50))
        self.btn9.setFont(font2)

        self.gridLayout.addWidget(self.btn9, 3, 2, 1, 1)

        self.btn6 = QPushButton(self.tabSettings)
        self.grpDigits.addButton(self.btn6)
        self.btn6.setObjectName(u"btn6")
        self.btn6.setMinimumSize(QSize(50, 50))
        self.btn6.setMaximumSize(QSize(50, 50))
        self.btn6.setFont(font2)

        self.gridLayout.addWidget(self.btn6, 2, 2, 1, 1)

        self.btn1 = QPushButton(self.tabSettings)
        self.grpDigits.addButton(self.btn1)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setMinimumSize(QSize(50, 50))
        self.btn1.setMaximumSize(QSize(50, 50))
        self.btn1.setFont(font2)

        self.gridLayout.addWidget(self.btn1, 1, 0, 1, 1)

        self.btnClear = QPushButton(self.tabSettings)
        self.grpActions.addButton(self.btnClear)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setMinimumSize(QSize(50, 50))
        self.btnClear.setMaximumSize(QSize(50, 50))
        self.btnClear.setFont(font2)

        self.gridLayout.addWidget(self.btnClear, 4, 2, 1, 1)

        self.btnDot = QPushButton(self.tabSettings)
        self.grpActions.addButton(self.btnDot)
        self.btnDot.setObjectName(u"btnDot")
        self.btnDot.setMinimumSize(QSize(50, 50))
        self.btnDot.setMaximumSize(QSize(50, 50))
        self.btnDot.setFont(font2)

        self.gridLayout.addWidget(self.btnDot, 4, 1, 1, 1)

        self.btnRS = QPushButton(self.tabSettings)
        self.grpActions.addButton(self.btnRS)
        self.btnRS.setObjectName(u"btnRS")
        self.btnRS.setMinimumSize(QSize(50, 50))
        self.btnRS.setMaximumSize(QSize(50, 50))
        self.btnRS.setFont(font2)

        self.gridLayout.addWidget(self.btnRS, 0, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)


        self.horizontalLayout_11.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_3 = QSpacerItem(422, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_11.setStretch(2, 1)
        self.tabWidget.addTab(self.tabSettings, "")

        self.horizontalLayout_9.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Metar Decoder", None))
        self.lblAirportCode.setText(QCoreApplication.translate("MainWindow", u"Airport code:", None))
        self.lblArrow.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"HPA", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MM", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"INCH", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMetar), QCoreApplication.translate("MainWindow", u"Metar Decoder", None))
        self.lblLanguage.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.lblQuickbar.setText(QCoreApplication.translate("MainWindow", u"Quickbar", None))
        self.btnQuickbarMinus.setText("")
        self.btnQuickbarPlus.setText("")
        self.btnSaveSettings.setText(QCoreApplication.translate("MainWindow", u"Save settings", None))
        self.btnLS.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.btnDel.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.btnPlus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btnStepen.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.btnUmno.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.btn8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btnMinus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btnRes.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btn9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btnClear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btnDot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.btnRS.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSettings), QCoreApplication.translate("MainWindow", u"Calculator + Settings", None))
    # retranslateUi


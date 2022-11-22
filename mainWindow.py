# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QButtonGroup, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        font = QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabMetar = QWidget()
        self.tabMetar.setObjectName(u"tabMetar")
        self.verticalLayout_2 = QVBoxLayout(self.tabMetar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.tabMetar)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.edtAirportCode = QLineEdit(self.tabMetar)
        self.edtAirportCode.setObjectName(u"edtAirportCode")

        self.horizontalLayout.addWidget(self.edtAirportCode)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tblResult = QTableWidget(self.tabMetar)
        self.tblResult.setObjectName(u"tblResult")
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tblResult.setSelectionMode(QAbstractItemView.NoSelection)
        self.tblResult.setTextElideMode(Qt.ElideNone)
        self.tblResult.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tblResult.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tblResult.verticalHeader().setVisible(False)

        self.horizontalLayout_5.addWidget(self.tblResult)

        self.lblBall = QLabel(self.tabMetar)
        self.lblBall.setObjectName(u"lblBall")

        self.horizontalLayout_5.addWidget(self.lblBall)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.tabMetar, "")
        self.tabCalculator = QWidget()
        self.tabCalculator.setObjectName(u"tabCalculator")
        self.verticalLayout_4 = QVBoxLayout(self.tabCalculator)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.tabCalculator)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.edtHPA = QLineEdit(self.tabCalculator)
        self.edtHPA.setObjectName(u"edtHPA")

        self.horizontalLayout_4.addWidget(self.edtHPA)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 14)

        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.tabCalculator)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.edtMMRT = QLineEdit(self.tabCalculator)
        self.edtMMRT.setObjectName(u"edtMMRT")

        self.horizontalLayout_2.addWidget(self.edtMMRT)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 14)

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.tabCalculator)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.edtENCHRT = QLineEdit(self.tabCalculator)
        self.edtENCHRT.setObjectName(u"edtENCHRT")

        self.horizontalLayout_3.addWidget(self.edtENCHRT)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 14)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.edtExpression = QLineEdit(self.tabCalculator)
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
        self.btnLS = QPushButton(self.tabCalculator)
        self.grpActions = QButtonGroup(MainWindow)
        self.grpActions.setObjectName(u"grpActions")
        self.grpActions.addButton(self.btnLS)
        self.btnLS.setObjectName(u"btnLS")
        self.btnLS.setMinimumSize(QSize(50, 50))
        self.btnLS.setMaximumSize(QSize(50, 50))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(False)
        self.btnLS.setFont(font1)

        self.gridLayout.addWidget(self.btnLS, 0, 0, 1, 1)

        self.btnRS = QPushButton(self.tabCalculator)
        self.grpActions.addButton(self.btnRS)
        self.btnRS.setObjectName(u"btnRS")
        self.btnRS.setMinimumSize(QSize(50, 50))
        self.btnRS.setMaximumSize(QSize(50, 50))
        self.btnRS.setFont(font1)

        self.gridLayout.addWidget(self.btnRS, 0, 1, 1, 1)

        self.btnStepen = QPushButton(self.tabCalculator)
        self.grpActions.addButton(self.btnStepen)
        self.btnStepen.setObjectName(u"btnStepen")
        self.btnStepen.setMinimumSize(QSize(50, 50))
        self.btnStepen.setMaximumSize(QSize(50, 50))
        self.btnStepen.setFont(font1)

        self.gridLayout.addWidget(self.btnStepen, 0, 2, 1, 1)

        self.btnPlus = QPushButton(self.tabCalculator)
        self.grpActions.addButton(self.btnPlus)
        self.btnPlus.setObjectName(u"btnPlus")
        self.btnPlus.setMinimumSize(QSize(50, 50))
        self.btnPlus.setMaximumSize(QSize(50, 50))
        self.btnPlus.setFont(font1)

        self.gridLayout.addWidget(self.btnPlus, 0, 3, 1, 1)

        self.btn1 = QPushButton(self.tabCalculator)
        self.grpDigits = QButtonGroup(MainWindow)
        self.grpDigits.setObjectName(u"grpDigits")
        self.grpDigits.addButton(self.btn1)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setMinimumSize(QSize(50, 50))
        self.btn1.setMaximumSize(QSize(50, 50))
        self.btn1.setFont(font1)

        self.gridLayout.addWidget(self.btn1, 1, 0, 1, 1)

        self.btn2 = QPushButton(self.tabCalculator)
        self.grpDigits.addButton(self.btn2)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setMinimumSize(QSize(50, 50))
        self.btn2.setMaximumSize(QSize(50, 50))
        self.btn2.setFont(font1)

        self.gridLayout.addWidget(self.btn2, 1, 1, 1, 1)

        self.btn3 = QPushButton(self.tabCalculator)
        self.grpDigits.addButton(self.btn3)
        self.btn3.setObjectName(u"btn3")
        self.btn3.setMinimumSize(QSize(50, 50))
        self.btn3.setMaximumSize(QSize(50, 50))
        self.btn3.setFont(font1)

        self.gridLayout.addWidget(self.btn3, 1, 2, 1, 1)

        self.btnMinus = QPushButton(self.tabCalculator)
        self.grpActions.addButton(self.btnMinus)
        self.btnMinus.setObjectName(u"btnMinus")
        self.btnMinus.setMinimumSize(QSize(50, 50))
        self.btnMinus.setMaximumSize(QSize(50, 50))
        self.btnMinus.setFont(font1)

        self.gridLayout.addWidget(self.btnMinus, 1, 3, 1, 1)

        self.btn4 = QPushButton(self.tabCalculator)
        self.grpDigits.addButton(self.btn4)
        self.btn4.setObjectName(u"btn4")
        self.btn4.setMinimumSize(QSize(50, 50))
        self.btn4.setMaximumSize(QSize(50, 50))
        self.btn4.setFont(font1)

        self.gridLayout.addWidget(self.btn4, 2, 0, 1, 1)

        self.btn5 = QPushButton(self.tabCalculator)
        self.grpDigits.addButton(self.btn5)
        self.btn5.setObjectName(u"btn5")
        self.btn5.setMinimumSize(QSize(50, 50))
        self.btn5.setMaximumSize(QSize(50, 50))
        self.btn5.setFont(font1)

        self.gridLayout.addWidget(self.btn5, 2, 1, 1, 1)

        self.btn6 = QPushButton(self.tabCalculator)
        self.grpDigits.addButton(self.btn6)
        self.btn6.setObjectName(u"btn6")
        self.btn6.setMinimumSize(QSize(50, 50))
        self.btn6.setMaximumSize(QSize(50, 50))
        self.btn6.setFont(font1)

        self.gridLayout.addWidget(self.btn6, 2, 2, 1, 1)

        self.btnUmno = QPushButton(self.tabCalculator)
        self.grpActions.addButton(self.btnUmno)
        self.btnUmno.setObjectName(u"btnUmno")
        self.btnUmno.setMinimumSize(QSize(50, 50))
        self.btnUmno.setMaximumSize(QSize(50, 50))
        self.btnUmno.setFont(font1)

        self.gridLayout.addWidget(self.btnUmno, 2, 3, 1, 1)

        self.btn7 = QPushButton(self.tabCalculator)
        self.grpDigits.addButton(self.btn7)
        self.btn7.setObjectName(u"btn7")
        self.btn7.setMinimumSize(QSize(50, 50))
        self.btn7.setMaximumSize(QSize(50, 50))
        self.btn7.setBaseSize(QSize(50, 50))
        self.btn7.setFont(font1)

        self.gridLayout.addWidget(self.btn7, 3, 0, 1, 1)

        self.btn8 = QPushButton(self.tabCalculator)
        self.grpDigits.addButton(self.btn8)
        self.btn8.setObjectName(u"btn8")
        self.btn8.setMinimumSize(QSize(50, 50))
        self.btn8.setMaximumSize(QSize(50, 50))
        self.btn8.setFont(font1)

        self.gridLayout.addWidget(self.btn8, 3, 1, 1, 1)

        self.btn9 = QPushButton(self.tabCalculator)
        self.grpDigits.addButton(self.btn9)
        self.btn9.setObjectName(u"btn9")
        self.btn9.setMinimumSize(QSize(50, 50))
        self.btn9.setMaximumSize(QSize(50, 50))
        self.btn9.setFont(font1)

        self.gridLayout.addWidget(self.btn9, 3, 2, 1, 1)

        self.btnDel = QPushButton(self.tabCalculator)
        self.grpActions.addButton(self.btnDel)
        self.btnDel.setObjectName(u"btnDel")
        self.btnDel.setMinimumSize(QSize(50, 50))
        self.btnDel.setMaximumSize(QSize(50, 50))
        self.btnDel.setFont(font1)

        self.gridLayout.addWidget(self.btnDel, 3, 3, 1, 1)

        self.btn0 = QPushButton(self.tabCalculator)
        self.grpDigits.addButton(self.btn0)
        self.btn0.setObjectName(u"btn0")
        self.btn0.setMinimumSize(QSize(50, 50))
        self.btn0.setMaximumSize(QSize(50, 50))
        self.btn0.setFont(font1)

        self.gridLayout.addWidget(self.btn0, 4, 0, 1, 1)

        self.btnDot = QPushButton(self.tabCalculator)
        self.grpActions.addButton(self.btnDot)
        self.btnDot.setObjectName(u"btnDot")
        self.btnDot.setMinimumSize(QSize(50, 50))
        self.btnDot.setMaximumSize(QSize(50, 50))
        self.btnDot.setFont(font1)

        self.gridLayout.addWidget(self.btnDot, 4, 1, 1, 1)

        self.btnClear = QPushButton(self.tabCalculator)
        self.grpActions.addButton(self.btnClear)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setMinimumSize(QSize(50, 50))
        self.btnClear.setMaximumSize(QSize(50, 50))
        self.btnClear.setFont(font1)

        self.gridLayout.addWidget(self.btnClear, 4, 2, 1, 1)

        self.btnRes = QPushButton(self.tabCalculator)
        self.grpActions.addButton(self.btnRes)
        self.btnRes.setObjectName(u"btnRes")
        self.btnRes.setMinimumSize(QSize(50, 50))
        self.btnRes.setMaximumSize(QSize(50, 50))
        self.btnRes.setFont(font1)

        self.gridLayout.addWidget(self.btnRes, 4, 3, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.verticalLayout_4.setStretch(3, 1)
        self.tabWidget.addTab(self.tabCalculator, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Metar Decoder", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Airport code:", None))
        self.lblBall.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMetar), QCoreApplication.translate("MainWindow", u"Metar Decoder", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"HPA", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MM", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"INCH", None))
        self.btnLS.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.btnRS.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.btnStepen.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.btnPlus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btnMinus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btnUmno.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.btn7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btnDel.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.btn0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btnDot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.btnClear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btnRes.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCalculator), QCoreApplication.translate("MainWindow", u"Calculator", None))
    # retranslateUi


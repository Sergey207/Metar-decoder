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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QSizePolicy,
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
        self.verticalLayout_2.setSpacing(20)
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

        self.tblResult = QTableWidget(self.tabMetar)
        self.tblResult.setObjectName(u"tblResult")
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tblResult.setSelectionMode(QAbstractItemView.NoSelection)
        self.tblResult.setTextElideMode(Qt.ElideNone)
        self.tblResult.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tblResult.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tblResult.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.tblResult)

        self.tabWidget.addTab(self.tabMetar, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.edtQNH = QLineEdit(self.tab_2)
        self.edtQNH.setObjectName(u"edtQNH")

        self.horizontalLayout_4.addWidget(self.edtQNH)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 15)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.edtQFE = QLineEdit(self.tab_2)
        self.edtQFE.setObjectName(u"edtQFE")

        self.horizontalLayout_3.addWidget(self.edtQFE)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 15)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.edtQNE = QLineEdit(self.tab_2)
        self.edtQNE.setObjectName(u"edtQNE")

        self.horizontalLayout_2.addWidget(self.edtQNE)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 15)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_2, "")

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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMetar), QCoreApplication.translate("MainWindow", u"Metar Decoder", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"QNH", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"QFE", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"QNE", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Calculator", None))
    # retranslateUi


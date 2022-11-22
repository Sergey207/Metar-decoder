import pathlib
import sys
from pprint import pprint

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLineEdit, QButtonGroup, QPushButton
from PythonMETAR import Metar as M, NOAAServError
from metar.Metar import Metar

from mainWindow import Ui_MainWindow

TEST_DATA = [
    "UUWW", "UUEE", "KJFK"
]
APP_DIR = pathlib.Path(__file__).parent

DEBUG = '.idea1' in map(lambda x: x.name, APP_DIR.iterdir())
TIME_TO_ERROR_MESSAGE = 2000  # milliseconds


class Window(QMainWindow, Ui_MainWindow):
    EXPRESSION_SYMBOLS = '1234567890()^:*+-. '

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.edtAirportCode.textChanged.connect(self.onAirportCodeChanged)
        self.edtHPA.textChanged.connect(self.onQChanged)
        self.edtMMRT.textChanged.connect(self.onQChanged)
        self.edtENCHRT.textChanged.connect(self.onQChanged)
        self.grpDigits.buttonClicked.connect(self.onDigitalClick)
        self.grpActions.buttonClicked.connect(self.onActionClick)

        self.isEditing = False

        self.tblResult.setRowCount(10)
        self.tblResult.setColumnCount(2)
        self.tblResult.setHorizontalHeaderLabels(("Name", "Value"))

        self.updateTableSize()
        if DEBUG:
            self.edtAirportCode.setText('UUWW')

    def check_expression(self) -> bool:
        return all([i in self.EXPRESSION_SYMBOLS for i in self.edtExpression.text()])

    def resolveExpression(self):
        if not self.check_expression():
            self.statusBar.showMessage('Wrong expression!', TIME_TO_ERROR_MESSAGE)
            return
        e = self.edtExpression.text()
        e = e.replace(':', '/')
        if '^' in e:
            e = '(' + e
            e = e.replace('^', ')**(')
            e += ')'
        self.edtExpression.setText(str(float(eval(e))))

    def onDigitalClick(self, sender: QPushButton):
        if not isinstance(sender, QPushButton):
            return
        self.edtExpression.setText(self.edtExpression.text() + sender.text())

    def onActionClick(self, sender: QPushButton):
        if not isinstance(sender, QPushButton):
            return
        if sender == self.btnClear:
            self.edtExpression.clear()
        elif sender == self.btnRes:
            self.resolveExpression()
        else:
            self.edtExpression.setText(self.edtExpression.text() + sender.text())

    def onQChanged(self):
        if self.isEditing:
            return
        self.isEditing = True

        sender: QLineEdit = self.sender()
        if not isinstance(sender, QLineEdit):
            self.isEditing = False
            return
        text = sender.text().replace(',', '.')
        if text == '':
            self.edtHPA.clear()
            self.edtMMRT.clear()
            self.edtENCHRT.clear()

        try:
            text = float(text)
        except ValueError:
            self.isEditing = False
            self.statusBar.showMessage('Uncorrect input data!', TIME_TO_ERROR_MESSAGE)
            return
        if sender == self.edtHPA:
            self.edtMMRT.setText(str(text * 0.750064))
            self.edtENCHRT.setText(str(text * 0.02953))
        elif sender == self.edtMMRT:
            self.edtHPA.setText(str(text * 1.33322390232))
            self.edtENCHRT.setText(str(text * 0.039370068943645))
        elif sender == self.edtENCHRT:
            self.edtHPA.setText(str(text * 33.86389))
            self.edtMMRT.setText(str(text * 25.40000632032))
        self.isEditing = False

    def updateTableSize(self):
        self.tblResult.setColumnWidth(0, 200)
        self.tblResult.setColumnWidth(1, 540)

    def onAirportCodeChanged(self):
        if len(self.edtAirportCode.text()) == 4:
            self.updateMetar()

    def updateMetar(self):
        try:
            metar = M(self.edtAirportCode.text().upper())
            metar_text = metar.metar.split()
        except NOAAServError:
            self.statusBar.showMessage('Error updating metar data -> check your internet and code!',
                                       TIME_TO_ERROR_MESSAGE)
            return
        m = Metar(' '.join(metar_text))

        self.tblResult.setItem(0, 0, QTableWidgetItem('Airport code'))
        self.tblResult.setItem(0, 1, QTableWidgetItem(str(m.station_id)))

        self.tblResult.setItem(1, 0, QTableWidgetItem('Date and time'))
        self.tblResult.setItem(1, 1, QTableWidgetItem(str(m.time)))

        self.tblResult.setItem(2, 0, QTableWidgetItem('Wind direction and speed'))
        self.tblResult.setItem(2, 1, QTableWidgetItem(f"Direction: {m.wind_dir} Speed: {m.wind_speed}"))

        self.tblResult.setItem(3, 0, QTableWidgetItem('Visibility'))
        self.tblResult.setItem(3, 1, QTableWidgetItem(str(m.visibility('M'))))

        self.tblResult.setItem(4, 0, QTableWidgetItem('Weather'))
        self.tblResult.setItem(4, 1, QTableWidgetItem(str(metar.weather)))  # TODO

        self.tblResult.setItem(5, 0, QTableWidgetItem('Overcast'))
        self.tblResult.setItem(5, 1, QTableWidgetItem(str('OVC 006')))  # TODO

        self.tblResult.setItem(6, 0, QTableWidgetItem('Wind Temperatures'))
        self.tblResult.setItem(6, 1, QTableWidgetItem(f'Temperature: {m.temp} Dewpoint: {m.dewpt}'))

        self.tblResult.setItem(7, 0, QTableWidgetItem('Altimeter setting'))
        self.tblResult.setItem(7, 1, QTableWidgetItem(f'{m.press}'))

        self.tblResult.setItem(8, 0, QTableWidgetItem('Forecast'))
        self.tblResult.setItem(8, 1, QTableWidgetItem(f'{m.max_temp_24hr}'))  # TODO

        self.tblResult.setItem(9, 0, QTableWidgetItem('Metar text'))
        self.tblResult.setItem(9, 1, QTableWidgetItem(str(m.code)))


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(f'{APP_DIR.absolute() / "Icon.png"}'))
    window = Window()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()

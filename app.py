import pathlib
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLineEdit, QPushButton
from PythonMETAR import Metar as M, NOAAServError
from metar.Metar import Metar

from ArrowLabel import ArrowLabel
from mainWindow import Ui_MainWindow
from CONSTANTS import *

TEST_DATA = [
    "UUWW", "UUEE", "KJFK"
]
APP_DIR = pathlib.Path(__file__).parent

DEBUG = '.idea' in map(lambda x: x.name, APP_DIR.iterdir())
TIME_TO_ERROR_MESSAGE = 2000  # milliseconds


class Window(QMainWindow, Ui_MainWindow):
    EXPRESSION_SYMBOLS = '1234567890()^:*+-. '

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        arrLabel = ArrowLabel()
        self.horizontalLayout_5.replaceWidget(self.lblArrow, arrLabel)
        self.lblArrow.deleteLater()
        self.lblArrow = arrLabel

        self.edtAirportCode.textChanged.connect(self.onAirportCodeChanged)
        self.edtHPA.textChanged.connect(self.onQChanged)
        self.edtMMRT.textChanged.connect(self.onQChanged)
        self.edtENCHRT.textChanged.connect(self.onQChanged)
        self.grpDigits.buttonClicked.connect(self.onDigitalClick)
        self.grpActions.buttonClicked.connect(self.onActionClick)
        self.edtExpression.returnPressed.connect(self.resolveExpression)

        self.isEditing = False

        self.tblResult.setRowCount(9)
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
        if e != '':
            self.edtExpression.setText(str(float(eval(e))))
        else:
            self.edtExpression.setText('0')

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
        self.tblResult.setColumnWidth(1, 601)

    def onAirportCodeChanged(self):
        if len(self.edtAirportCode.text()) == 4:
            self.updateMetar()

    def updateMetar(self):
        try:
            metar = M(self.edtAirportCode.text().upper())
            metar_text: list[str] = metar.metar.split()
        except NOAAServError:
            self.statusBar.showMessage('Error updating metar data -> check your internet and code!',
                                       TIME_TO_ERROR_MESSAGE)
            return
        m = Metar(' '.join(metar_text))
        to_show: list[tuple[str, str]] = []

        to_show.append(('Airport code', str(m.station_id)))
        to_show.append(('Date and time', str(m.time)))
        to_show.append(('Wind direction and speed', f"Direction: {m.wind_dir} Speed: {m.wind_speed}"))
        to_show.append(('Visibility', str(m.visibility())))

        for code in metar_text:
            res = []
            if code[0] in ('-', '+'):
                res.append(weather_prefixes[code[0]])
                code = code[1:]
            if code in weathers_codes.keys():
                res.append(weathers_codes[code])
                to_show.append(('Weather', ' '.join(res)))

        for i in metar_text:
            if i[:3] in CLOUDS:
                to_show.append(('Sky conditions', i))
            elif i[:2] == 'CB':
                to_show.append(('Sky conditions', i))

        to_show.append(('Wind Temperatures', f'Temperature: {m.temp} Dewpoint: {m.dewpt}'))
        to_show.append(('Altimeter setting', str(m.press)))

        self.tblResult.clear()
        self.tblResult.setHorizontalHeaderLabels(('Name', 'Value'))
        self.tblResult.setRowCount(len(to_show))
        for index, line in enumerate(to_show):
            self.tblResult.setItem(index, 0, QTableWidgetItem(line[0]))
            self.tblResult.setItem(index, 1, QTableWidgetItem(line[1]))

        self.edtMetarCode.setText(m.code)
        self.lblArrow.setDeg(metar.wind['direction'])
        self.lblArrow.repaint()


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(f'{APP_DIR.absolute() / "Icon.png"}'))
    window = Window()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()

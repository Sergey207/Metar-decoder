import sys
from pprint import pprint

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLineEdit
from PythonMETAR import Metar as M, NOAAServError
from metar.Metar import Metar

from mainWindow import Ui_MainWindow

TEST_DATA = [
    "UUWW", "UUEE", "KJFK"
]

DEBUG = True


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.edtAirportCode.textChanged.connect(self.onAirportCodeChanged)
        self.edtHPA.textChanged.connect(self.onQChanged)
        self.edtMMRT.textChanged.connect(self.onQChanged)
        self.edtENCHRT.textChanged.connect(self.onQChanged)

        self.tblResult.setRowCount(10)
        self.tblResult.setColumnCount(2)
        self.tblResult.setHorizontalHeaderLabels(("Name", "Value", "Code"))

        self.updateTableSize()
        if DEBUG:
            self.edtAirportCode.setText('UUWW')
            # self.onAirportCodeChanged()

    def updateTableSize(self):
        self.tblResult.setColumnWidth(0, 200)
        self.tblResult.setColumnWidth(1, 400)
        self.tblResult.setColumnWidth(2, 150)
        # self.tblResult.setColumnWidth(0, 100)
        # self.tblResult.setColumnWidth(1, 10)

    def onQChanged(self):
        sender: QLineEdit = self.sender()
        if not isinstance(sender, QLineEdit):
            return
        text = sender.text().replace(',', '.')
        if text == '':
            self.edtHPA.clear()
            self.edtMMRT.clear()
            self.edtENCHRT.clear()

        try:
            text = float(text)
        except ValueError:
            self.statusBar.showMessage('Uncorrect input data!', 5000)
            return
        if sender == self.edtHPA:
            self.edtMMRT.setText(str(text * 0.750064))
            self.edtENCHRT.setText(str(text * 0.02953))

    def onAirportCodeChanged(self):
        if len(self.edtAirportCode.text()) == 4:
            self.updateMetar()

    def updateMetar(self):
        try:
            metar = M(self.edtAirportCode.text().upper())
            # metar = M(self.edtAirportCode.text())
            metar_text = metar.metar.split()
        except NOAAServError:
            self.statusBar.showMessage('Error updating metar data -> check your internet and code!', 5000)
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


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()

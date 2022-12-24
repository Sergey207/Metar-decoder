import pathlib
import sys

import requests
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLineEdit, QPushButton

from Designs.arrowLabel import ArrowLabel
from Designs.mainWindow import Ui_MainWindow
from metar.metarEngine import Metar

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
        self.tblResult.setColumnWidth(0, 350)
        self.tblResult.setColumnWidth(1, 420)

    def onAirportCodeChanged(self):
        if len(self.edtAirportCode.text()) == 4:
            self.updateMetar()

    def updateMetar(self):
        self.tblResult.clear()
        self.tblResult.setHorizontalHeaderLabels(('Name', 'Value'))
        try:
            metar = Metar(self.edtAirportCode.text().upper())
        except ValueError:
            self.status_bar.showMessage("Value Error -> Error airport code", TIME_TO_ERROR_MESSAGE)
            return
        except requests.RequestException:
            self.status_bar.showMessage("Internet Error -> Check your internet connection or Airport code",
                                        TIME_TO_ERROR_MESSAGE)
            return

        to_show: list[tuple[str, str]] = []

        to_show.append(('Airport code', metar.airport_code))
        to_show.append(('Airport name', metar.name))
        to_show.append(('Date and time', metar.date_time.strftime("%d/%m/%Y %H:%M:%S")))
        for i in range(len(metar.wind)):
            name_prefix = f" {i + 1}" if len(metar.wind) > 1 else ''
            wind = metar.wind[i]

            to_show.append((f'Wind direction' + name_prefix, f"{wind.direction}°"))
            to_show.append(("Wind speed", f"{wind.speed} {wind.unit_of_measurement}"))
            if wind.gust:
                to_show.append(("Wind gust" + name_prefix, f"{wind.gust} {wind.unit_of_measurement}"))

        for i in range(len(metar.visibility)):
            visibility = metar.visibility[i]
            name_prefix = f" {i + 1}" if len(metar.visibility) > 1 else ""

            if visibility.direction != 'CAVOK':
                to_show.append(("Visibility" + name_prefix, "> 10 km"))
            else:
                to_show.append(("Visibility" + name_prefix,
                                f"Distance: {visibility.distance} Direction: {visibility.direction}"))

        # for i in range(len(metar.vpp_visibility)):
        #     vpp_visibility = metar.vpp_visibility[i]
        #     name_prefix = f" {i + 1}" if len(metar.vpp_visibility) > 1 else ""

        for i, rvr_weather in enumerate(metar.rvr_weather):
            name = f"RVR {rvr_weather.RVR_number}"
            if rvr_weather.RVR_parallel:
                name += f" parralel {rvr_weather.RVR_parallel}"

            if rvr_weather.visibility_prefix:
                to_show.append((name + ' visibility prefix', f'{rvr_weather.visibility_prefix}'))

            to_show.append((name + ' runway deposit', str(rvr_weather.runway_deposit)))
            to_show.append((name + ' extend of contamination', str(rvr_weather.extend_of_contamination)))
            to_show.append((name + ' depth of deposit', str(rvr_weather.depth_of_deposit)))
            to_show.append((name + ' braking friction coeficient', str(rvr_weather.braking_friction_coeficient)))

        for i, weather in enumerate(metar.weather):
            name = f'Weather {i + 1}' if len(metar.weather) > 1 else 'Weather'
            if weather.intensivity:
                to_show.append((name + ' intensivity', weather.intensivity))
            if weather.descriptor:
                to_show.append((name + ' descriptor', weather.descriptor))
            if weather.precipitations[0]:
                to_show.append((name + ' precipitations', weather.precipitations[0]))
            if weather.precipitations[1]:
                to_show.append((name + ' precipitations', weather.precipitations[1]))
            if weather.bad_visibility_weather_events:
                to_show.append((name + ' bad visibility weather events', weather.bad_visibility_weather_events))
            if weather.other_weather_events:
                to_show.append((name + ' other weather events', weather.other_weather_events))

        for i, cloudiness in enumerate(metar.cloudiness):
            name_prefix = f' {i + 1}' if len(metar.cloudiness) > 1 else ''
            to_show.append(('Cloudiness' + name_prefix, f'Высота {cloudiness.height_of_lower_bound} метров; '
                                                        f'{cloudiness.number_of_clouds}'))

        for i, temperature_dewpoint in enumerate(metar.temperature_and_dewpoint):
            name_prefix = f' {i + 1}' if len(metar.cloudiness) > 1 else ''
            to_show.append(('Temperature' + name_prefix, f'{temperature_dewpoint.temperature}°'))
            to_show.append(('Dewpoint' + name_prefix, f'{temperature_dewpoint.dewpoint}°'))

        for i, pressure in enumerate(metar.pressure):
            name_prefix = f' {i + 1}' if len(metar.pressure) > 1 else ''
            to_show.append(('Pressure' + name_prefix, str(pressure.QNH) + ' QNH'))

        self.tblResult.setRowCount(len(to_show))
        for index, line in enumerate(to_show):
            self.tblResult.setItem(index, 0, QTableWidgetItem(line[0]))
            self.tblResult.setItem(index, 1, QTableWidgetItem(line[1]))

        self.edtMetarCode.setText(metar.metar)
        if metar.wind:
            self.lblArrow.setDeg(metar.wind[0].direction)
            self.lblArrow.repaint()


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(f'{APP_DIR.absolute() / "Icon.png"}'))
    window = Window()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()

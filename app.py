import json
import pathlib
import sys

import requests
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLineEdit, QPushButton

from Designs.arrowLabel import ArrowLabel
from Designs.mainWindow import Ui_MainWindow
from metar.metarEngine import Metar


class Window(QMainWindow, Ui_MainWindow):
    EXPRESSION_SYMBOLS = '1234567890()^:*+-. '

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cmbLanguage.addItems(("english", "russian"))
        self.cmbLanguage.setCurrentText(language)

        for airport_code in quick_bar[::-1]:
            new_button = QPushButton(self)
            new_button.setText(airport_code)
            new_button.clicked.connect(self.onQuickBarButtonClick)
            self.lytQuickBar.insertWidget(0, new_button)
        arr_label = ArrowLabel(self.lblArrow.width(), self.lblArrow.height())
        self.horizontalLayout_5.replaceWidget(self.lblArrow, arr_label)
        self.lblArrow.deleteLater()
        self.lblArrow = arr_label

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

    def onQuickBarButtonClick(self):
        sender = self.sender()
        if not isinstance(sender, QPushButton):
            return
        self.edtAirportCode.setText(sender.text())

    def check_expression(self) -> bool:
        return all([i in self.EXPRESSION_SYMBOLS for i in self.edtExpression.text()])

    def resolveExpression(self):
        if not self.check_expression():
            self.edtExpression.setText('Error!')
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

    @staticmethod
    def get_table_data(metar: Metar):
        to_show: list[tuple[str, str]] = [
            (app_locale['Airport code'], metar.airport_code),
            (app_locale['Airport name'], metar.name),
            (app_locale['Date and time'], metar.date_time.strftime("%d/%m/%Y %H:%M:%S"))
        ]

        for i, wind in enumerate(metar.wind):
            name_prefix = f" {i + 1}" if len(metar.wind) > 1 else ''

            to_show.append((app_locale['Wind direction'] + name_prefix, f"{wind.direction}°"))
            to_show.append((app_locale['Wind speed'] + name_prefix, f"{wind.speed} {wind.unit_of_measurement}"))
            if wind.gust:
                to_show.append((app_locale['Wind gust'] + name_prefix, f"{wind.gust} {wind.unit_of_measurement}"))

        for i, visibility in enumerate(metar.visibility):
            if len(metar.visibility) > 1:
                name = f"{app_locale['Visibility']} {i + 1}"
            else:
                name = app_locale['Visibility']

            new_str = visibility.distance
            if visibility.direction:
                new_str += f' {visibility.direction}'
            to_show.append((name, new_str))

        for i, rvr_weather in enumerate(metar.rvr_weather):
            name = f"{app_locale['RVR']} {rvr_weather.RVR_number}"
            if rvr_weather.RVR_parallel:
                name += f" {app_locale['parallel']} {RVR_prefixes.get(rvr_weather.RVR_parallel, not_found_message)}"

            if rvr_weather.visibility_prefix:
                to_show.append((name + ' ' + app_locale["visibility prefix"],
                                RVR_visibilty_prefixes.get(rvr_weather.visibility_prefix, not_found_message)
                                ))

            if rvr_weather.visibility_changes:
                to_show.append((name + ' ' + app_locale['visibility changes'],
                                RVR_visibility_changements_prefixes.get(
                                    rvr_weather.visibility_changes,
                                    not_found_message)
                                ))

            if rvr_weather.RVR_weather:
                to_show.append((name + ' ' + app_locale['weather'],
                                RVR_weathers.get(rvr_weather.RVR_weather, not_found_message)))

            if rvr_weather.runway_deposit:
                runway_deposit = RVR_deposits.get(rvr_weather.runway_deposit, not_found_message).capitalize()
                runway_deposit += f' ({rvr_weather.runway_deposit})'
                to_show.append((name + ' ' + app_locale['RVR deposit'], runway_deposit))

            if rvr_weather.extend_of_contamination:
                extend_of_contamination = RVR_extends_of_contamination.get(rvr_weather.extend_of_contamination,
                                                                           not_found_message)
                extend_of_contamination += f' ({rvr_weather.extend_of_contamination})'
                to_show.append((name + ' ' + app_locale['extend of contamination'], extend_of_contamination))

            if rvr_weather.depth_of_deposit:
                depth_of_deposit = RVR_deposits.get(rvr_weather.depth_of_deposit, not_found_message)
                depth_of_deposit += f' ({rvr_weather.depth_of_deposit})'
                to_show.append((name + ' ' + app_locale['depth of deposit'], depth_of_deposit))
            to_show.append((name + ' ' + app_locale['braking friction coefficient'],
                            str(rvr_weather.braking_friction_coeficient)))

        for i, weather in enumerate(metar.weather):
            name = f'{app_locale["Weather"]} {i + 1}' if len(metar.weather) > 1 else app_locale['Weather']
            if weather.intensivity:
                to_show.append((name + ' ' + app_locale['intensivity'],
                                intensivities.get(weather.intensivity, not_found_message)))
            if weather.descriptor:
                to_show.append((name + ' ' + app_locale['descriptor'],
                                descriptors.get(weather.descriptor, not_found_message)))
            if weather.precipitations[0]:
                to_show.append((name + ' ' + app_locale['precipitations'],
                                precipitations.get(weather.precipitations[0], not_found_message)))
            if weather.precipitations[1]:
                to_show.append((name + ' precipitations',
                                precipitations.get(weather.precipitations[1], not_found_message)))
            if weather.bad_visibility_weather_events:
                to_show.append((name + ' ' + app_locale['bad visibility weather events'],
                                bad_visibility_weather_events.get(
                                    weather.bad_visibility_weather_events, not_found_message
                                )))
            if weather.other_weather_events:
                to_show.append((name + ' ' + app_locale['other weather events'],
                                other_weather_events.get(weather.other_weather_events, not_found_message)))

        for i, clouds in enumerate(metar.cloudiness):
            if len(metar.cloudiness) > 1:
                name = f'{app_locale["Cloudiness"]} {i + 1}'
            else:
                name = app_locale['Cloudiness']
            new_str = cloudiness.get(clouds.number_of_clouds, not_found_message)
            if clouds.height_of_lower_bound:
                new_str = f'{app_locale["Height"]} {clouds.height_of_lower_bound} m; ' + new_str
            to_show.append((name, new_str))

        for i, temperature_dewpoint in enumerate(metar.temperature_and_dewpoint):
            name_prefix = f' {i + 1}' if len(metar.temperature_and_dewpoint) > 1 else ''
            to_show.append((app_locale['Temperature'] + name_prefix, f'{temperature_dewpoint.temperature}°'))
            to_show.append((app_locale['Dewpoint'] + name_prefix, f'{temperature_dewpoint.dewpoint}°'))

        for i, pressure in enumerate(metar.pressure):
            name_prefix = f' {i + 1}' if len(metar.pressure) > 1 else ''
            to_show.append((app_locale['Pressure'] + name_prefix,
                            f"{pressure.value} {pressure.unit_of_measurement}"))
        return to_show

    def updateMetar(self):
        self.tblResult.clear()
        self.tblResult.setHorizontalHeaderLabels((app_locale['Name'], app_locale['Value']))
        try:
            metar = Metar(self.edtAirportCode.text().upper())
        except ValueError:
            self.edtMetarCode.setText(value_error)
            return
        except requests.RequestException:
            self.edtMetarCode.setText(internet_error)
            return

        to_show = self.get_table_data(metar)

        self.tblResult.setRowCount(len(to_show))
        for index, line in enumerate(to_show):
            self.tblResult.setItem(index, 0, QTableWidgetItem(line[0]))
            self.tblResult.setItem(index, 1, QTableWidgetItem(line[1]))

        self.edtMetarCode.setText(metar.metar)
        # if metar.wind:
        #     self.lblArrow.setDeg(metar.wind[0].direction)
        #     self.lblArrow.repaint()
        self.tblResult.resizeColumnsToContents()


def load_settings():
    settings_path = APP_DIR / 'settings.json'
    if not settings_path.exists():
        return DEFAULT_SETTINGS
    with settings_path.open() as f:
        try:
            result = json.load(f)
        except json.JSONDecodeError:
            return DEFAULT_SETTINGS

        if 'language' not in result or 'quick_bar' not in result:
            return DEFAULT_SETTINGS
        if not isinstance(result['language'], str) or not isinstance(result['quick_bar'], list):
            return DEFAULT_SETTINGS
        for i in result['quick_bar']:
            if not isinstance(i, str):
                return DEFAULT_SETTINGS
    return result


TEST_DATA = [
    "UUWW", "UUEE", "KJFK", "URWW"
]
APP_DIR = pathlib.Path(__file__).parent
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    EXE_DIR = pathlib.Path(getattr(sys, '_MEIPASS'))
else:
    EXE_DIR = APP_DIR
DEBUG = '.idea' in map(lambda x: x.name, APP_DIR.iterdir())

DEFAULT_SETTINGS = {
    "language": "english",
    "quick_bar": ["UUWW", "UUEE", "URWW", "KJFK"]
}
settings = load_settings()
language = settings['language']
quick_bar = settings['quick_bar']
if language.lower() in ('ru', 'rus', 'russian'):
    from metar.metarConstantsRussian import *
else:
    from metar.metarConstantsEnglish import *


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(f'{APP_DIR.absolute() / "Icon.png"}'))
    window = Window()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()

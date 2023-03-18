import json
import pathlib
import sys
from getpass import getuser

import requests
import zulu
from PySide6.QtCore import QTimer
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLineEdit, QPushButton, QListWidgetItem

from Designs.arrowLabel import ArrowLabel
from Designs.mainWindow import Ui_MainWindow
from MetarEngine.metarEnLocalization import EnLocale
from MetarEngine.metarEngine import Metar
from tableGenerators import *


class Window(QMainWindow, Ui_MainWindow):
    lblArrow: ArrowLabel
    starOff: QIcon
    starOn: QIcon
    star_state: bool
    timer_metars: QTimer
    timer_time: QTimer

    def __init__(self):
        super().__init__()
        self.setup_ui()

        self.edtPressures = (self.edtHPA, self.edtMMRT, self.edtENCHRT)
        self.edtDistance = (self.edtM, self.edtKM, self.edtNM)
        self.edtSpeeds = (self.edtMPS, self.edtKT, self.edtKMH)
        self.edtAll = self.edtPressures + self.edtDistance + self.edtSpeeds

        self.setup_signals()
        self.setup_timers()
        self.update_time_event()

        self.isEditing = False

    def setup_ui(self):
        self.setupUi(self)

        self.cmbLanguage.addItems(("english", "russian"))
        self.cmbLanguage.setCurrentText(language)

        self.lstQuickbar.addItems(quick_bar)
        self.lstQuickbar.itemClicked.connect(self.onQuickBarButtonClick)

        arr_label = ArrowLabel(self.lblArrow.width(), self.lblArrow.height())
        self.horizontalLayout_5.replaceWidget(self.lblArrow, arr_label)
        self.lblArrow.deleteLater()
        self.lblArrow = arr_label

        self.starOff = QIcon(f"{APP_DIR.absolute() / 'Icons' / 'StarOff.png'}")
        self.starOn = QIcon(f"{APP_DIR.absolute() / 'Icons' / 'StarOn.png'}")
        self.btnAddToQuickbar.setIcon(self.starOff)
        self.star_state = False

        self.lblAirportCode.setText(app_locale.Airport_code)

    def setup_signals(self):
        self.edtAirportCode.textChanged.connect(self.onAirportCodeChanged)
        self.cmbLanguage.currentTextChanged.connect(self.onLanguageChanged)
        self.btnAddToQuickbar.clicked.connect(self.onAddToQuickbarClicked)

        for edt in self.edtAll:
            edt.textChanged.connect(self.onEdtConverterChanged)

    def setup_timers(self):
        self.timer_metars = QTimer()
        self.timer_metars.timeout.connect(self.onAirportCodeChanged)
        self.timer_metars.start(900000)

        self.timer_time = QTimer()
        self.timer_time.timeout.connect(self.update_time_event)
        self.timer_time.start(1000)

    def setup_table_size(self):
        self.tblResult.clear()
        self.tblResult.setColumnCount(2)
        self.tblResult.setRowCount(0)
        self.tblResult.setHorizontalHeaderLabels((app_locale.Name, app_locale))

    def update_time_event(self):
        zulu_time = zulu.now()
        time_now = datetime.datetime.now().time()
        self.lblTimeZULU.setText(zulu_time.strftime("ZULU: %H:%M"))
        self.lblTimeUTC.setText(time_now.strftime(f"UTC: %H:%M"))

    def onEdtConverterChanged(self):
        if self.isEditing:
            return
        self.isEditing = True

        sender: QLineEdit = self.sender()
        if not isinstance(sender, QLineEdit):
            self.isEditing = False
            return

        text = sender.text().replace(',', '.')
        if text == '':
            if sender in self.edtPressures:
                for edt in self.edtPressures:
                    edt.clear()
            elif sender in self.edtDistance:
                for edt in self.edtDistance:
                    edt.clear()
            elif sender in self.edtSpeeds:
                for edt in self.edtSpeeds:
                    edt.clear()
            self.isEditing = False
            return

        try:
            text = float(text)
        except ValueError:
            self.isEditing = False
            return

        if sender in self.edtPressures:
            if sender == self.edtHPA:
                self.edtMMRT.setText(str(text * 0.750064))
                self.edtENCHRT.setText(str(text * 0.02953))
            elif sender == self.edtMMRT:
                self.edtHPA.setText(str(text * 1.33322390232))
                self.edtENCHRT.setText(str(text * 0.039370068943645))
            elif sender == self.edtENCHRT:
                self.edtHPA.setText(str(text * 33.86389))
                self.edtMMRT.setText(str(text * 25.40000632032))
        elif sender in self.edtDistance:
            if sender == self.edtM:
                self.edtKM.setText(str(text * 0.001))
                self.edtNM.setText(str(text * 0.00062137119))
            elif sender == self.edtKM:
                self.edtM.setText(str(text * 1000))
                self.edtNM.setText(str(text * 0.62137119224))
            elif sender == self.edtNM:
                self.edtM.setText(str(text * 1609.344))
                self.edtKM.setText(str(text * 1.609344))
        elif sender in self.edtSpeeds:
            if sender == self.edtMPS:
                self.edtKT.setText(str(text * 1.94384))
                self.edtKMH.setText(str(text * 3.6))
            elif sender == self.edtKT:
                self.edtMPS.setText(str(text * 0.5144))
                self.edtKMH.setText(str(text * 1.85199))
            elif sender == self.edtKMH:
                self.edtMPS.setText(str(text * 0.27777))
                self.edtKT.setText(str(text * 0.53995))

        for edt in self.edtAll:
            if edt == sender:
                continue
            text = edt.text()
            if not text:
                continue
            text = float(text.replace(',', '.'))
            if text == 0:
                edt.setText('0')
            else:
                edt.setText(format(text, '.2f'))

        self.isEditing = False

    def onQuickBarButtonClick(self, item: QListWidgetItem):
        if not isinstance(item, QListWidgetItem):
            return
        self.edtAirportCode.setText(item.text())
        self.check_star_state()

    def onLanguageChanged(self):
        global language
        language = self.cmbLanguage.currentText()
        self.save_settings()

    def onAirportCodeChanged(self):
        self.check_star_state()
        if len(self.edtAirportCode.text()) == 4:
            self.updateMetar()

    def onAddToQuickbarClicked(self):
        sender: QPushButton = self.sender()
        if not isinstance(sender, QPushButton):
            return
        text = self.edtAirportCode.text().upper()

        if self.star_state:
            quick_bar.remove(text)
            self.save_settings()
            for i in range(self.lstQuickbar.count()):
                if self.lstQuickbar.item(i).text() == text:
                    self.lstQuickbar.takeItem(self.lstQuickbar.row(self.lstQuickbar.item(i)))
                    break
            for i in self.lstQuickbar.selectedItems():
                i.setSelected(False)
            self.set_star_state(False)
        else:
            if len(text) != 4:
                return

            text = text.upper()
            quick_bar.append(text)
            self.save_settings()

            self.lstQuickbar.addItem(text)
            for i in range(self.lstQuickbar.count()):
                item = self.lstQuickbar.item(i)
                item.setSelected(item.text() == self.edtAirportCode.text().upper())
            self.set_star_state(True)
        self.check_star_state()

    def check_star_state(self):
        for item in self.lstQuickbar.selectedItems():
            if item.text() != self.edtAirportCode.text().upper():
                item.setSelected(False)
                continue
            self.edtAirportCode.setText(item.text())
            self.set_star_state(True)
            return
        for i in range(self.lstQuickbar.count()):
            item = self.lstQuickbar.item(i)
            if item.text() == self.edtAirportCode.text().upper():
                item.setSelected(True)
                self.set_star_state(True)
                return
        self.set_star_state(False)

    def set_star_state(self, state):
        self.btnAddToQuickbar.setIcon(self.starOn if state else self.starOff)
        self.star_state = state

    def setup_columns_size(self):
        self.tblResult.resizeColumnsToContents()
        width = max(self.tblResult.width() - self.tblResult.columnWidth(0) - 2, self.tblResult.columnWidth(1))
        self.tblResult.setColumnWidth(1, width)

    @staticmethod
    def save_settings():
        settings_path = pathlib.Path(f'C:/Users/{getuser()}/AppData/Local/MetarDecoder')
        if not settings_path.exists():
            settings_path.mkdir()
        settings_path /= 'settings.json'
        with settings_path.open('w') as f:
            json.dump({'language': language, 'quick_bar': quick_bar}, f, indent=2)

    def get_table_data(self, metar: Metar):
        to_show: list[tuple[str, str]] = [
            (app_locale.Airport_code, metar.airport_code),
            (app_locale.Airport_name, metar.name),
            (app_locale.Date_and_time, metar.date_time.strftime("%d/%m/%Y %H:%M:%S"))
        ]

        self.lblArrow.resetDeg()
        to_show.extend(generate_wind(metar.wind, app_locale, self))
        self.lblArrow.repaint()

        to_show.extend(generate_visibility(metar.visibility, app_locale, self))

        to_show.extend(generate_rvr_visibility(metar.rvr_visibility, app_locale))

        to_show.extend(generate_rvr_weather(metar.rvr_weather, app_locale))

        to_show.extend(generate_weather(metar.weather, app_locale))

        to_show.extend(generate_cloudiness(metar.cloudiness, app_locale))

        to_show.extend(generate_temp_dewpoint(metar.temperature_and_dewpoint, app_locale))

        to_show.extend(generate_pressure(metar.pressure, app_locale, self))

        if metar.trend:
            to_show.append((app_locale.Trend, app_locale.trends.get(metar.trend.split()[0], app_locale.not_found_message)))
            if metar.trend_time:
                trend_time_text = [f"{app_locale.trend_time.get(i.type_of_trend_time)} {i.time.strftime('%H:%M')}" for i in metar.trend_time]
                to_show.append((app_locale.Trend + '; ' + app_locale.time, ' '.join(trend_time_text)))

            to_show.extend(generate_wind(metar.trend_wind, app_locale))

            to_show.extend(generate_visibility(metar.trend_visibility, app_locale))

            to_show.extend(generate_cloudiness(metar.trend_cloudiness, app_locale, is_trend=True))

        return to_show

    def updateMetar(self):
        self.setup_table_size()
        try:
            metar = Metar(self.edtAirportCode.text().upper())
        except ValueError:
            self.edtMetarCode.setText(app_locale.internet_error)
            self.tblResult.clear()
            return
        except requests.RequestException:
            self.edtMetarCode.setText(app_locale.internet_error)
            self.tblResult.clear()
            return

        to_show = self.get_table_data(metar)

        self.tblResult.setRowCount(len(to_show))
        for index, line in enumerate(to_show):
            self.tblResult.setItem(index, 0, QTableWidgetItem(line[0]))
            self.tblResult.setItem(index, 1, QTableWidgetItem(line[1]))

        self.edtMetarCode.setText(metar.full_metar)
        self.setup_columns_size()

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.setup_columns_size()


def load_settings():
    settings_path = pathlib.Path(f'C:/Users/{getuser()}/AppData/Local/MetarDecoder')
    if not settings_path.exists():
        return DEFAULT_SETTINGS
    settings_path /= 'settings.json'
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


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(f'{APP_DIR.absolute() / "Icons" / "Icon.png"}'))
    window = Window()
    window.show()
    app.exec()


if __name__ == '__main__':
    APP_DIR = pathlib.Path(__file__).parent
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        EXE_DIR = pathlib.Path(sys.executable).parent
    else:
        EXE_DIR = APP_DIR

    DEFAULT_SETTINGS = {
        "language": "english",
        "quick_bar": ["UUWW", "UUEE", "URWW", "KJFK"]
    }
    settings = load_settings()
    language = settings['language']
    quick_bar = settings['quick_bar']
    if language.lower() in ('ru', 'rus', 'russian'):
        app_locale = RuLocale()
    else:
        app_locale = EnLocale()

    main()

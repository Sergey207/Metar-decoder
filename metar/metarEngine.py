import datetime
import re

import requests

from metar.metarClasses import *
from metar.metarConstants import weather_regular_expression, cloudiness_re


class Metar:
    metars_server = 'https://metartaf.ru/'
    backup_metars_server = 'https://beta.aviationweather.gov/cgi-bin/data/metar.php'
    trend_split = ('NOSIG', 'BECMG', 'TEMPO', 'NSW', 'FM', 'TL', 'AT')

    def __init__(self, airport_code: str, custom_server_data: dict[str, str] = None):
        if not custom_server_data:
            if not isinstance(airport_code, str) or len(airport_code) != 4:
                raise ValueError
            self.airport_code = airport_code
            self.server_data = self.get_server_data()
        else:
            self.airport_code = custom_server_data['icao']
            self.server_data = custom_server_data

        self.name = self.server_data['name']

        metar = self.server_data['metar'].split()
        self.full_metar = ' '.join(metar)

        self.metar = metar
        self.trend = []
        self.remarks = []

        for i in self.trend_split:
            if i in metar:
                index = metar.index(i)
                self.metar = metar[:index]
                self.trend = metar[index:]
                break

        if self.trend:
            if 'RMK' in self.trend:
                index = self.trend.index('RMK')
                self.trend = self.trend[:index]
                self.remarks = self.trend[index:]
        else:
            if 'RMK' in self.metar:
                index = self.metar.index('RMK')
                self.metar = metar[:index]
                self.remarks = metar[index:]

        self.metar = ' '.join(self.metar)
        self.trend = ' '.join(self.trend)
        self.remarks = ' '.join(self.remarks)

        self.taf = ' '.join(self.server_data['taf'].split())

        self.date_time = self.analyze_date_time()
        self.wind = self.analyze_wind_gust()
        self.visibility = self.analyze_visibility()
        self.rvr_visibility = self.analyze_rvr_visibility()
        self.rvr_weather = self.analyze_rvr_weather()
        self.weather = self.analyze_weather()
        self.cloudiness = self.analyze_cloudiness()
        self.temperature_and_dewpoint = self.analyze_temperature_devpoint()
        self.pressure = self.analyze_pressure()
        self.trend = [self.trend]

    def get_server_data(self):
        response = requests.get(self.metars_server + self.airport_code + '.json')
        if not response:
            raise requests.RequestException
        return response.json()

    def analyze_date_time(self):
        s = self.metar.split()
        return datetime.datetime(*map(int, s[0].split('-')), *map(int, s[1].split(':')))

    def analyze_wind_gust(self):
        res = []
        for i in re.findall(r'(VRB|\d{3})(P\d{2}|\d{2})(G\d{2}|)(MPS|KMH|KT)', self.metar):
            res.append(Wind(*i))
        return res

    def analyze_visibility(self):
        res = []
        re_expressions = (r'\s(\d{4}|\d{1,2}SM)(W|S|E|N|)\s', r'\s(\d{4}|\d{2}SM)(NW|NE|SW|SE)\s', '(CAVOK)()')
        for re_expr in re_expressions:
            for i in re.findall(re_expr, self.metar):
                res.append(Visibility(*i))
        return res

    def analyze_rvr_visibility(self):
        res = []
        for i in re.findall(r'R(\d{2})(L|C|R|)/(M|P|)(\d{4})(U|N|D|)', self.metar):
            res.append(RVRVisibility(i[0], i[1], i[2], i[3], i[4]))
        return res

    def analyze_rvr_weather(self):
        res = []
        for i in re.findall(r'R(\d{2})(L|C|R|)/(M|P|)(\d{4}|CLSD|CLRD|SNOKLO)(\d{2})(U|D|N|)', self.metar):
            res.append(RVRWeather(i[0], i[1], i[2], i[3], i[4], i[5]))
        return res

    def analyze_weather(self):
        res = []
        for i in re.findall(weather_regular_expression, self.metar):
            if any(i):
                res.append(Weather(*i))
        return res

    def analyze_cloudiness(self):
        res = []
        for i in re.findall(cloudiness_re, self.metar):
            res.append(Cloudiness(*i))
        return res

    def analyze_temperature_devpoint(self):
        res = []
        for i in re.findall(r'\s(M|)(\d{2})/(M|)(\d{2})\s', self.metar):
            res.append(TemperatureDewpoint(*i))
        return res

    def analyze_pressure(self):
        res = []
        for i in re.findall(r'([QA])(\d{4})', self.metar):
            res.append(Pressure(*i))
        return res

    def __str__(self):
        return ' '.join(self.metar.split())

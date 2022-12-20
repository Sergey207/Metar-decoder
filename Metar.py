import datetime
import re
from pprint import pprint

import requests

from metarConstants import *
from MetarClasses import *


class Metar:
    metars_server = 'https://tgftp.nws.noaa.gov/data/observations/metar/stations/'

    def __init__(self, airport_code: str):
        if not isinstance(airport_code, str) or len(airport_code) != 4:
            raise ValueError

        self.airport_code = airport_code
        self.metar = self.get_metar()
        self.date_time = self.analyze_date_time()
        self.wind = self.analyze_wind_gust()
        self.visibility = self.analyze_visibility()
        self.vpp_visibility = self.analyze_vpp_visibility()
        self.rvr_weather = self.analyze_rvr_weather()
        self.weather = self.analyze_weather()
        self.cloudiness = self.analyze_cloudiness()
        self.temperature_and_dewpoint = self.analyze_temperature_devpoint()
        self.pressure = self.analyze_pressure()
        self.add_info = self.analyze_add_info()

    def get_metar(self):
        response = requests.get(self.metars_server + self.airport_code + '.TXT')
        if not response:
            raise requests.RequestException
        return ' '.join(response.text.split())

    def analyze_date_time(self):
        s = self.metar.split()
        return datetime.datetime(*map(int, s[0].split('/')), *map(int, s[1].split(':')))

    def analyze_wind_gust(self):
        res = []
        for i in re.findall(r'(VRB|\d{3})(P\d{2}|\d{2})(G\d{2}|)(MPS|KT)', self.metar):
            res.append(Wind(*i))
        return res

    def analyze_visibility(self):
        res = []
        re_expressions = (r'\s(\d{4})(W|S|E|N|)\s', r'\s(\d{4})(NW|NE|SW|SE)\s', '(CAVOK)()')
        for re_expr in re_expressions:
            for i in re.findall(re_expr, self.metar):
                res.append(Visibility(*i))
        return res

    def analyze_vpp_visibility(self):
        res = []
        for i in re.findall(r'R(\d{2})([LCR]?)/([PM]?)(\d{4})([UDN]?)', self.metar):
            # print(i)
            pass  # TODO
        return res

    def analyze_rvr_weather(self):
        res = []
        for i in re.findall(r'R(\d{2})(L|C|R|)/(M|P|)(\d)(\d)(\d{2})(\d{2})(U|D|N|)', self.metar):
            res.append(RVRWeather(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
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
        for i in re.findall(r'Q(\d{4})', self.metar):
            res.append(Pressure(i))
        return res

    def analyze_add_info(self):
        res = []
        for i in re.findall(r'RE', self.metar):
            res.append({
                # TODO
            })
        return res

    def __str__(self):
        return ' '.join(self.metar.split())


if __name__ == '__main__':
    m = Metar('UUWW')
    print(m)
    # pprint(m.wind, sort_dicts=False)
    # print(Metar('UUWW'))
    # print(Metar('KJFK'))
    # print(Metar('UUYH'))

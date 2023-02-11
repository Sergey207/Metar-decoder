import datetime
import re

from MetarEngine.metarClasses import *
from MetarEngine.metarConstants import trend_start, weather_regular_expression, cloudiness_re


def analyze_metar(metar: str) -> (str, str, str):
    """
    Analyzes full metar of metar and returns metar, trend, remarks
    :param metar: metar of metar to analyze (without \n)
    :return: metar (str), trend (str), remarks (str)
    """
    metar = metar.split()
    trend = []
    remarks = []

    for i in trend_start:
        if i in metar:
            index = metar.index(i)
            trend = metar[index:]
            metar = metar[:index]
            break

    if trend:
        if 'RMK' in trend:
            index = trend.index('RMK')
            remarks = trend[index:]
            trend = trend[:index]
    else:
        if 'RMK' in metar:
            index = metar.index('RMK')
            remarks = metar[index:]
            metar = metar[:index]

    metar = ' '.join(metar)
    trend = ' '.join(trend)
    remarks = ' '.join(remarks)

    return metar, trend, remarks


def analyze_date_time(metar):
    for i in re.findall(r'(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})', metar):
        return datetime.datetime(*map(int, i))


def analyze_wind_gust(metar):
    res = []
    for i in re.findall(r'(VRB|\d{3})(P\d{2}|\d{2})(G\d{2}|)(MPS|KMH|KT)', metar):
        res.append(Wind(*i))
    return res


def analyze_visibility(metar):
    res = []
    re_expressions = (
        r'\s(\d{4}|\d{1,2}SM)(W|S|E|N|)\s',
        r'\s(\d{4}|\d{1,2}SM)(NW|NE|SW|SE)\s',
        '(CAVOK)()'
    )
    for re_expr in re_expressions:
        for i in re.findall(re_expr, metar):
            res.append(Visibility(*i))
    return res


def analyze_rvr_visibility(metar):
    res = []
    for i in re.findall(r'R(\d{2})(L|C|R|)/(M|P|)(\d{4})(U|N|D|)', metar):
        res.append(RVRVisibility(i[0], i[1], i[2], i[3], i[4]))
    return res


def analyze_rvr_weather(metar):
    res = []
    for i in re.findall(r'R(\d{2})(L|C|R|)/(M|P|)(\d{4}|CLSD|CLRD|SNOKLO)(\d{2})(U|D|N|)', metar):
        res.append(RVRWeather(i[0], i[1], i[2], i[3], i[4], i[5]))
    return res


def analyze_weather(metar):
    res = []
    for i in re.findall(weather_regular_expression, metar):
        if any(i):
            res.append(Weather(*i))
    return res


def analyze_cloudiness(metar):
    res = []
    for i in re.findall(cloudiness_re, metar):
        res.append(Cloudiness(*i))
    return res


def analyze_temperature_devpoint(metar):
    res = []
    for i in re.findall(r'\s(M|)(\d{2})/(M|)(\d{2})\s', metar):
        res.append(TemperatureDewpoint(*i))
    return res


def analyze_pressure(metar):
    res = []
    for i in re.findall(r'([QA])(\d{4})', metar):
        res.append(Pressure(*i))
    return res

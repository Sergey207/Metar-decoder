import requests

from MetarEngine.metarAnalyzators import *


class Metar:
    metars_server = 'https://metartaf.ru/'
    backup_metars_server = 'https://beta.aviationweather.gov/cgi-bin/data/metar.php'

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

        if self.server_data['metar'] == 'Информация по данной станции не доступна':
            raise requests.RequestException

        self.metar, self.trend, self.remarks = analyze_metar(' '.join(self.server_data['metar'].split()))
        self.full_metar = ' '.join(self.server_data['metar'].split())
        self.taf = ' '.join(self.server_data['taf'].split())

        # trend
        self.date_time = analyze_date_time(self.metar)
        self.wind = analyze_wind_gust(self.metar)
        self.visibility = analyze_visibility(self.metar)
        self.rvr_visibility = analyze_rvr_visibility(self.metar)
        self.rvr_weather = analyze_rvr_weather(self.metar)
        self.weather = analyze_weather(self.metar)
        self.cloudiness = analyze_cloudiness(self.metar)
        self.temperature_and_dewpoint = analyze_temperature_devpoint(self.metar)
        self.pressure = analyze_pressure(self.metar)

        # trend
        self.trend_time = analyze_time_of_trend(self.trend)
        self.trend_wind = analyze_wind_gust(self.trend)
        self.trend_visibility = analyze_visibility(self.trend)
        self.trend_cloudiness = analyze_cloudiness(self.trend)

        # TODO Remarks
        # print(self.remarks)

        # taf
        self.taf, self.taf_trend, self.taf_remarks = analyze_metar(self.taf)

        # print(self.taf)
        self.taf_date_time = analyze_date_time(self.taf)
        self.taf_action_time = analyze_action_time(self.taf)
        self.taf_wind = analyze_wind_gust(self.taf)
        self.taf_visibility = analyze_visibility(self.taf)
        self.taf_weather = analyze_weather(self.taf)
        self.taf_cloudiness = analyze_cloudiness(self.taf)
        self.taf_air_temperature = analyze_air_temperature(self.taf)

        # TODO Trend in taf

    def __str__(self):
        return self.full_metar

    def get_server_data(self):
        response = requests.get(self.metars_server + self.airport_code + '.json')
        if not response:
            raise requests.RequestException
        return response.json()

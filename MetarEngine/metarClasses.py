import datetime


class Wind:
    def __init__(self, direction, speed, gust, unit_of_measurement):
        """
        :param direction: 10000 if Variable
        :param speed: int
        :param gust: bool
        :param unit_of_measurement: MPS or KMH or KT
        """
        self.direction = int(direction) if direction != "VRB" else 10000
        self.speed = int(speed[-2:])
        self.speed_more_then_50mps = speed.startswith('P')
        self.gust = int(gust[1:]) if gust else 0
        self.unit_of_measurement = unit_of_measurement

    def __repr__(self):
        return f"Direction: {self.direction}, Speed: {self.speed}, " \
               f"Speed >50mps: {self.speed_more_then_50mps}, " \
               f"Gust: {self.gust}, Unit of measurement: {self.unit_of_measurement}"


class Visibility:
    def __init__(self, distance, direction):
        """
        :param distance: 10000 if CAVOK
        :param direction: "" if there is no direction
        """
        self.unit_of_measurement = 'm'
        if distance == 'CAVOK':
            self.distance = 10000
        else:
            if distance.endswith('SM'):
                distance = distance[:-2]
                self.unit_of_measurement = 'SM'
            self.distance = int(distance)
        self.direction = direction if direction else ""

    def __repr__(self):
        return f"Distance: {self.distance}, Direction: {self.direction}"


class RVRVisibility:
    def __init__(self, RVR_number, RVR_parallel, visibility_prefix, visibility, visibility_changes):
        """
        :param RVR_number: int
        :param RVR_parallel: str
        :param visibility_prefix: str
        :param visibility: int
        :param visibility_changes: str
        """
        self.RVR_number = RVR_number
        self.RVR_parallel = RVR_parallel
        self.visibility_prefix = visibility_prefix
        self.visibility = visibility
        self.visibility_changes = visibility_changes

    def __repr__(self):
        return f"""self.RVR_number = RVR_number
RVR_parallel = {self.RVR_parallel}
visibility_prefix = {self.visibility_prefix}
visibility = {self.visibility}
visibility_changes = {self.visibility_changes}"""


class RVRWeather:
    def __init__(self, RVR_number, RVR_parallel, visibility_prefix,
                 rvr_weather_info, braking_friction_coeficient, visibility_changes):
        self.RVR_number = int(RVR_number)
        self.RVR_parallel = RVR_parallel
        self.visibility_prefix = visibility_prefix

        if rvr_weather_info in ('CLSD', 'CLRD', 'SNOKLO'):
            self.RVR_weather = rvr_weather_info
            self.runway_deposit = None
            self.extend_of_contamination = None
            self.depth_of_deposit = None
        else:
            self.RVR_weather = None
            self.runway_deposit = rvr_weather_info[0]
            self.extend_of_contamination = rvr_weather_info[1]
            self.depth_of_deposit = str(int(rvr_weather_info[2:]))

        self.braking_friction_coeficient = int(braking_friction_coeficient) / 100
        self.visibility_changes = visibility_changes

    def __repr__(self):
        return f"""RVR_number = {self.RVR_number}
RVR_parallel = {self.RVR_parallel}
visibility_prefix = {self.visibility_prefix}
RVR_weather = {self.RVR_weather}
runway_deposit = {self.runway_deposit}
extend_of_contamination = {self.extend_of_contamination}
depth_of_deposit = {self.depth_of_deposit}
braking_friction_coeficient = {self.braking_friction_coeficient}
visibility_changes = {self.visibility_changes}"""


class Weather:
    def __init__(self, intensivity, descriptor, precipitation1, precipitation2,
                 bad_visibility_weather_event, other_weather_event):
        self.intensivity = intensivity
        self.descriptor = descriptor
        self.precipitations = (precipitation1, precipitation2)
        self.bad_visibility_weather_events = bad_visibility_weather_event
        self.other_weather_events = other_weather_event

    def __repr__(self):
        return f"Intensivity = {self.intensivity} " \
               f"Descriptor = {self.descriptor} " \
               f"Precipitation = {self.precipitations} " \
               f"Bad_visibility_weather_events = {self.bad_visibility_weather_events} " \
               f"Other_weather_events = {self.other_weather_events}"


class Cloudiness:
    def __init__(self, number_of_clouds, height_of_lower_bound):
        self.number_of_clouds = number_of_clouds
        if height_of_lower_bound:
            self.height_of_lower_bound = int(height_of_lower_bound) * 100
        else:
            self.height_of_lower_bound = None

    def __repr__(self):
        return f"Number_of_clouds = {self.number_of_clouds} " \
               f"Height_of_lower_bound = {self.height_of_lower_bound}"


class TemperatureDewpoint:
    def __init__(self, temperature_sign, temperature, dewpoint_sign, dewpoint):
        self.temperature = float(temperature) * (-1 if temperature_sign else 1)
        self.dewpoint = float(dewpoint) * (-1 if dewpoint_sign else 1)
        if temperature_sign and self.temperature == 0:
            self.temperature = -0.5
        if dewpoint_sign and self.dewpoint == 0:
            self.dewpoint = -0.5

    def __repr__(self):
        return f"Temperature = {self.temperature} Dewpoint = {self.dewpoint}"


class Pressure:
    units_of_measurement = {'Q': 'HPA', 'A': 'inHg'}

    def __init__(self, unit_of_measurement, value):
        self.value = str(int(value))
        if unit_of_measurement == 'A':
            self.value = format(int(self.value) / 100, '.2f')
        self.unit_of_measurement = self.units_of_measurement.get(unit_of_measurement)

    def __repr__(self):
        return f"{self.value} {self.unit_of_measurement}"


class TrendTime:
    def __init__(self, type_of_trend_time, hour, minute):
        self.type_of_trend_time = type_of_trend_time
        self.time = datetime.time(int(hour), int(minute))

    def __repr__(self):
        return f'{self.type_of_trend_time} -> {self.time}'


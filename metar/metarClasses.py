from metar.metarConstants import *


class Wind:
    def __init__(self, direction, speed, gust, unit_of_measurement):
        self.direction = int(direction) if direction != "VRB" else "Variable"
        self.speed = int(speed[-2:])
        self.speed_more_then_50mps = speed.startswith('P')
        self.gust = int(gust[1:]) if gust else None
        self.unit_of_measurement = unit_of_measurement

    def __repr__(self):
        return f"Direction: {self.direction}, Speed: {self.speed}, " \
               f"Speed > 50 mps: {self.speed_more_then_50mps} " \
               f"Gust: {self.gust}, Unit of measurement: {self.unit_of_measurement}"


class Visibility:
    def __init__(self, distance, direction):
        self.distance = int(distance) if distance != 'CAVOK' else distance
        self.direction = direction if direction else None

    def __repr__(self):
        return f"Distance: {self.distance}, Direction: {self.direction}"


class RVRWeather:
    def __init__(self, RVR_number, RVR_parallel, visibility_prefix, runway_deposit,
                 extend_of_contamination, depth_of_deposit, braking_friction_coeficient, visibility_changes):
        self.RVR_number = int(RVR_number)
        self.RVR_parallel = RVR_prefixes_english.get(RVR_parallel)
        self.visibility_prefix = RVR_visibilty_prefixes_english.get(visibility_prefix)
        self.runway_deposit = str(RVR_deposit_russian.get(runway_deposit)) + f' - {runway_deposit}'
        self.extend_of_contamination = RVR_extend_of_contamination_russian.get(extend_of_contamination)
        self.depth_of_deposit = str(int(depth_of_deposit)) + ' mm'
        self.braking_friction_coeficient = int(braking_friction_coeficient) / 100
        self.visibility_changes = RVR_visibility_changements_prefixes_english.get(visibility_changes)

    def __repr__(self):
        return f"RVR_number = {self.RVR_number} " \
               f"RVR_parallel = {self.RVR_parallel} " \
               f"visibility_prefix = {self.visibility_prefix} " \
               f"runway_deposit = {self.runway_deposit} " \
               f"extend_of_contamination = {self.extend_of_contamination} " \
               f"depth_of_deposit = {self.depth_of_deposit} " \
               f"braking_friction_coeficient = {self.braking_friction_coeficient} " \
               f"visibility_changes = {self.visibility_changes} "


class Weather:
    def __init__(self, intensivity, descriptor, precipitation1, precipitation2,
                 bad_visibility_weather_events, other_weather_events):
        self.intensivity = intensivity_english.get(intensivity)
        self.descriptor = descriptor_english.get(descriptor)
        self.precipitations = (precipitation_english.get(precipitation1),
                               precipitation_english.get(precipitation2))
        self.bad_visibility_weather_events = bad_visibility_weather_events_english.get(bad_visibility_weather_events)
        self.other_weather_events = other_weather_events_english.get(other_weather_events)

    def __repr__(self):
        return f"Intensivity = {self.intensivity} " \
               f"Descriptor = {self.descriptor} " \
               f"Precipitation = {self.precipitations} " \
               f"Bad_visibility_weather_events = {self.bad_visibility_weather_events} " \
               f"Other_weather_events = {self.other_weather_events} "


class Cloudiness:
    def __init__(self, number_of_clouds, height_of_lower_bound):
        self.number_of_clouds = cloudiness_russian.get(number_of_clouds)
        self.height_of_lower_bound = int(height_of_lower_bound) * 100

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
    def __init__(self, QNH):
        self.QNH = QNH

    def __repr__(self):
        return f"QNH = {self.QNH}"

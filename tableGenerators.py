from MetarEngine.metarClasses import *
from MetarEngine.metarRuLocalization import RuLocale


def generate_wind(winds: list[Wind], locale: RuLocale, app=None):
    res = []
    for i, wind in enumerate(winds):
        name_prefix = f" {i + 1}" if len(winds) > 1 else ''
        group_prefix = f"{locale.Trend}; " if app is None else ''

        res.append((group_prefix + locale.Wind_direction + name_prefix, f"{wind.direction}°"))
        wind_speed = f"{wind.speed} {wind.unit_of_measurement}"
        if wind.unit_of_measurement == 'KT':
            wind_speed += f' ({format(wind.speed * 0.51, ".2f")} m/c)'
        res.append((group_prefix + locale.Wind_speed + name_prefix, wind_speed))
        if wind.gust:
            res.append((group_prefix + locale.Wind_gust + name_prefix, f"{wind.gust} {wind.unit_of_measurement}"))

        if app is not None:
            app.lblArrow.setDeg(wind.direction)
            match wind.unit_of_measurement:
                case 'MPS':
                    app.edtMPS.setText(str(wind.speed))
                case 'KMH':
                    app.edtKMH.setText(str(wind.speed))
                case 'KT':
                    app.edtKT.setText(str(wind.speed))

    return res


def generate_visibility(visibilities: list[Visibility], locale: RuLocale, app=None):
    res = []
    for i, visibility in enumerate(visibilities):
        name_prefix = f'{locale.Visibility} {i + 1}' if len(visibilities) > 1 else locale.Visibility
        group_prefix = f'{locale.Trend}; ' if app is None else ''

        if visibility.distance < 9999:
            new_str = f'{visibility.distance} {visibility.unit_of_measurement}'
            if visibility.unit_of_measurement == 'SM':
                new_str += f' ({visibility.distance * 1852} m)'
        else:
            new_str = '>10km'

        if visibility.direction:
            new_str += f' {visibility.direction}'
        res.append((group_prefix + name_prefix, new_str))

        if app is not None:
            if visibility.unit_of_measurement == 'm':
                if visibility.distance == 9999:
                    app.edtM.setText('10000')
                else:
                    app.edtM.setText(str(visibility.distance))
            elif visibility.unit_of_measurement == 'SM':
                app.edtKM.setText(str(visibility.distance))
    return res


def generate_rvr_visibility(rvr_visibilities: list[RVRVisibility], locale: RuLocale):
    res = []
    for rvr_weather in rvr_visibilities:
        name = f"{locale.RVR} {rvr_weather.RVR_number}"
        if rvr_weather.RVR_parallel:
            name += f" {locale.Parallel} {locale.RVR_prefixes.get(rvr_weather.RVR_parallel, locale.not_found_message)}"
        name += '; '

        if rvr_weather.visibility_prefix:
            res.append(
                (
                    f"{name} {locale.Visibility_prefix}",
                    locale.RVR_visibilty_prefixes.get(rvr_weather.visibility_prefix, locale.not_found_message)
                )
            )

        if rvr_weather.visibility_changes:
            res.append(
                (
                    f'{name} {locale.Visibility_changes}',
                    locale.RVR_visibility_changements_prefixes.get(rvr_weather.visibility_changes, locale.not_found_message)
                )
            )
    return res


def generate_rvr_weather(rvr_weathers: list[RVRWeather], locale: RuLocale):
    res = []
    for i, rvr_weather in enumerate(rvr_weathers):
        name = f"{locale.RVR} {rvr_weather.RVR_number}"
        if rvr_weather.RVR_parallel:
            name += f" {locale.Parallel} {locale.RVR_prefixes.get(rvr_weather.RVR_parallel, locale.not_found_message)}"
        name += '; '

        if rvr_weather.visibility_prefix:
            res.append(
                (
                    f'{name} {locale.Visibility_prefix}',
                    locale.RVR_visibilty_prefixes.get(rvr_weather.visibility_prefix, locale.not_found_message)
                )
            )

        if rvr_weather.visibility_changes:
            res.append(
                (
                    name + ' ' + locale.Visibility_changes,
                    locale.RVR_visibility_changements_prefixes.get(rvr_weather.visibility_changes, locale.not_found_message)
                )
            )

        if rvr_weather.RVR_weather:
            res.append(
                (
                    f'{name} {locale.Weather}',
                    locale.RVR_weathers.get(rvr_weather.RVR_weather, locale.not_found_message)
                )
            )

        if rvr_weather.runway_deposit:
            runway_deposit = locale.RVR_deposits.get(rvr_weather.runway_deposit, locale.not_found_message).capitalize()
            runway_deposit += f' ({rvr_weather.runway_deposit})'
            res.append((name + ' ' + locale.RVR_deposit, runway_deposit))

        if rvr_weather.extend_of_contamination:
            extend_of_contamination = locale.RVR_extends_of_contamination.get(
                rvr_weather.extend_of_contamination, locale.not_found_message
            )
            extend_of_contamination += f' ({rvr_weather.extend_of_contamination})'
            res.append((f'{name} {locale.Extend_of_contamination}', extend_of_contamination))

        if rvr_weather.depth_of_deposit:
            depth_of_deposit = locale.RVR_deposits.get(rvr_weather.depth_of_deposit, locale.not_found_message)
            depth_of_deposit += f' ({rvr_weather.depth_of_deposit})'
            res.append((f'{name} {locale.Depth_of_deposit}', depth_of_deposit))
        res.append((f'{name} {locale.Braking_friction_coefficient}',
                    str(rvr_weather.braking_friction_coeficient)))
    return res


def generate_weather(weathers: list[Weather], locale: RuLocale):
    res = []
    for i, weather in enumerate(weathers):
        name = f'{locale.Weather} {i + 1}' if len(weathers) > 1 else locale.Weather
        if weather.intensivity:
            res.append((name + ' ' + locale.Intensivity,
                        locale.intensivities.get(weather.intensivity, locale.not_found_message)))
        if weather.descriptor:
            res.append((name + ' ' + locale.Descriptor,
                        locale.descriptors.get(weather.descriptor, locale.not_found_message)))
        if weather.precipitations[0]:
            res.append((name + ' ' + locale.Precipitations,
                        locale.precipitations.get(weather.precipitations[0], locale.not_found_message)))
        if weather.precipitations[1]:
            res.append((name + ' ' + locale.Precipitations,
                        locale.precipitations.get(weather.precipitations[1], locale.not_found_message)))
        if weather.bad_visibility_weather_events:
            res.append((name + ' ' + locale.Bad_visibility_weather_events,
                        locale.bad_visibility_weather_events.get(weather.bad_visibility_weather_events, locale.not_found_message)))
        if weather.other_weather_events:
            res.append((name + ' ' + locale.Other_weather_events,
                        locale.other_weather_events.get(weather.other_weather_events, locale.not_found_message)))
    return res


def generate_cloudiness(clouds: list[Cloudiness], locale: RuLocale, is_trend=False):
    res = []
    for i, cloud in enumerate(clouds):
        name_prefix = f'{locale.Cloudiness} {i + 1}' if len(clouds) > 1 else locale.Cloudiness
        group_prefix = f'{locale.Trend}; ' if is_trend else ''
        new_str = locale.cloudiness.get(cloud.number_of_clouds, locale.not_found_message)
        if cloud.height_of_lower_bound:
            new_str = f'{locale.Height} {cloud.height_of_lower_bound} m; ' + new_str
        res.append((group_prefix + name_prefix, new_str))
    return res


def generate_temp_dewpoint(temperature_and_dewpoint: list[TemperatureDewpoint], locale: RuLocale):
    res = []
    for i, temperature_dewpoint in enumerate(temperature_and_dewpoint):
        name_prefix = f' {i + 1}' if len(temperature_and_dewpoint) > 1 else ''
        res.append((locale.Temperature + name_prefix, f'{temperature_dewpoint.temperature}°'))
        res.append((locale.Dewpoint + name_prefix, f'{temperature_dewpoint.dewpoint}°'))
    return res


def generate_pressure(pressures: list[Pressure], locale: RuLocale, app):
    res = []
    for i, pressure in enumerate(pressures):
        name_prefix = f' {i + 1}' if len(pressures) > 1 else ''
        res.append((locale.Pressure + name_prefix,
                    f"{pressure.value} {pressure.unit_of_measurement}"))
        if pressure.unit_of_measurement == 'HPA':
            app.edtHPA.setText(pressure.value)
        if pressure.unit_of_measurement == 'inHg':
            app.edtENCHRT.setText(pressure.value)
    return res

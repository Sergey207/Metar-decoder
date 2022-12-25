from metar.metarConstantsEnglish import descriptor, precipitation, bad_visibility_weather_events, other_weather_events, \
    cloudiness

intensivity_re = [r'\-', r'\+', 'VC', '']
descriptor_re = descriptor.keys()
precipitation_re = precipitation.keys()
bad_visibility_weather_events_re = bad_visibility_weather_events.keys()
other_weather_events_re = other_weather_events.keys()

weather_regular_expression = r'\s' + f'({"|".join(intensivity_re)})' \
                                     f'({"|".join(descriptor_re)})?' \
                                     f'({"|".join(precipitation_re)})?' \
                                     f'({"|".join(precipitation_re)})?' \
                                     f'({"|".join(bad_visibility_weather_events_re)})?' \
                                     f'({"|".join(other_weather_events_re)})?' + \
                             r'\s'
cloudiness_re = '(' + '|'.join(cloudiness.keys()) + '|VV)' + r'(\d{3})'

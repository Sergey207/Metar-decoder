from MetarEngine.metarEnLocalization import EnLocale

intensivity_re = [r'\-', r'\+', 'VC', '']
descriptor_re = EnLocale.descriptors.keys()
precipitation_re = EnLocale.precipitations.keys()
bad_visibility_weather_events_re = EnLocale.bad_visibility_weather_events.keys()
other_weather_events_re = EnLocale.other_weather_events.keys()

weather_regular_expression = f'({"|".join(intensivity_re)})' \
                             f'({"|".join(descriptor_re)})?' \
                             f'({"|".join(precipitation_re)})?' \
                             f'({"|".join(precipitation_re)})?' \
                             f'({"|".join(bad_visibility_weather_events_re)})?' \
                             f'({"|".join(other_weather_events_re)})?'
weather_regular_expression = r'\s' + weather_regular_expression + r'\s'
cloudiness_re = '(' + '|'.join(EnLocale.cloudiness.keys()) + '|VV)' + r'(\d{3}|)'
trend_start = ('NOSIG', 'BECMG', 'TEMPO', 'NSW', 'FM', 'TL', 'AT')

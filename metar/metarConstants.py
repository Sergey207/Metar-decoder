intensivity_english = {
    '-': 'Light',
    '': 'Moderate',
    '+': 'Heavy',
    'VC': 'In the vicinity'
}
intensivity_russian = {
    '-': 'Слабая',
    '': 'Умеренная',
    '+': 'Сильная',
    'VC': 'Вблизи'
}

descriptor_english = {
    'MI': 'Shallow',
    'BC': 'Patches',
    'PR': 'Partial',
    'DR': 'Low drifting',
    'BL': 'Blowing',
    'SH': 'Shower',
    'TS': 'Thunderstorm',
    'FZ': 'Freezing'
}
descriptor_russian = {
    'MI': 'Тонкий (поземный)',
    'BC': 'Обрывки, клочья',
    'PR': 'Частичный',
    'DR': 'Поземок',
    'BL': 'Низовая',
    'SH': 'Ливень (ливни)',
    'TS': 'Гроза',
    'FZ': 'Замерзающий'
}

precipitation_english = {
    'DZ': 'Drizzle',
    'RA': 'Rain',
    'SN': 'Snow',
    'SG': 'Snow grains',
    'IC': 'Ice crystals',
    'PL': 'Ice pellets',
    'GR': 'Hail',
    'GS': 'Small hail and/or snow pellets',
    'UP': 'Unknown precipitation'
}
precipitation_russian = {
    'DZ': 'Морось',
    'RA': 'Дождь',
    'SN': 'Снег',
    'SG': 'Снежные зерна',
    'IC': 'Ледяные кристаллы/иглы',
    'PL': 'Ледяная крупа',
    'GR': 'Град',
    'GS': 'Мелкий град и/или снежная крупа',
    'UP': 'Неизвестные осадки'
}

bad_visibility_weather_events_english = {
    'BR': 'Mist',
    'FG': 'Fog',
    'FU': 'Smoke',
    'VA': 'Volcanic ash',
    'DU': 'Widespread dust',
    'SA': 'Sand',
    'HZ': 'Haze',
}
bad_visibility_weather_events_russian = {
    'BR': 'Дымка',
    'FG': 'Туман',
    'FU': 'Дым',
    'VA': 'Вулканический пепел',
    'DU': 'Пыль обложная',
    'SA': 'Песок',
    'HZ': 'Мгла',
}

other_weather_events_english = {
    'PO': 'Dust/sand whirls',
    'SQ': 'Squalls',
    'FC': 'Funnel cloud(s) (tornado or water spout)',
    'SS': 'Sandstorm',
    'DS': 'Duststorm'
}
other_weather_events_russian = {
    'PO': 'Пыльные/песчаные вихри',
    'SQ': 'Шквалы',
    'FC': 'Воронкообразное(ые) облако(а) (торнадо или водяной смерч)',
    'SS': 'Песчаная буря',
    'DS': 'Пыльная буря'
}

RVR_prefixes_english = {
    'L': 'Left',
    'C': 'Center',
    'R': 'Right'
}
RVR_prefixes_russian = {
    'L': 'Левая',
    'C': 'Центральная',
    'R': 'Правая'
}

RVR_visibilty_prefixes_english = {
    'P': 'Longer then 2000 m',
    'M': 'Shorter then minimal value'
}

RVR_visibilty_prefixes_russian = {
    'P': 'Длиннее чем 2000 метров',
    'M': 'Меньше минимального значения'
}

RVR_visibility_changements_prefixes_english = {
    'U': 'Increase of visibility',
    'D': 'Decrease of visibility',
    'N': 'No changes of visibility'
}
RVR_visibility_changements_prefixes_russian = {
    'U': 'Увеличение видимости',
    'D': 'Уменьшение видимости',
    'N': 'Нет изменений в видимости'
}

RVR_deposit_russian = {
    '0': 'Чисто и сухо',
    '1': 'Влажно',
    '2': 'Мокро',
    '4': 'Иней изморозь',
    '5': 'Мокрый снег',
    '6': 'Слякоть',
    '7': 'Лёд',
    '8': 'Укатанный снег',
    '9': 'Мёрзлая неровная ВПП'
}

RVR_extend_of_contamination_russian = {
    '1': '<10%',
    '2': '11-25%',
    '5': '26-51%',
    '9': '51-100%',
}

intensivity_re = [r'\-', r'\+', 'VC', '']
descriptor_re = descriptor_english.keys()
precipitation_re = precipitation_english.keys()
bad_visibility_weather_events_re = bad_visibility_weather_events_english.keys()
other_weather_events_re = other_weather_events_english.keys()

weather_regular_expression = r'\s' + f'({"|".join(intensivity_re)})' \
                                     f'({"|".join(descriptor_re)})?' \
                                     f'({"|".join(precipitation_re)})?' \
                                     f'({"|".join(precipitation_re)})?' \
                                     f'({"|".join(bad_visibility_weather_events_re)})?' \
                                     f'({"|".join(other_weather_events_re)})?' + \
                             r'\s'

cloudiness_russian = {
    "VV": "Состояние неба не определяется, например, не видно из-за тумана и/или других явлений",
    "FEW": "Несколько, 1-2 октанта",
    "SCT": "Разбросанные, 3-4 октанта",
    "BKN": "Значительные, 5-7 октантов",
    "OVC": "Сплошные, 8 октантов",
    "NSC": "Нет значимой для полетов облачности",
    "NCD": "Нет облачности; используется, когда автоматическая система не обнаружила облаков"
}
cloudiness_re = '(' + '|'.join(cloudiness_russian.keys()) + '|VV)' + r'(\d{3})'

class RuLocale:
    intensivities = {
        '-': 'Слабая',
        '': 'Умеренная',
        '+': 'Сильная',
        'VC': 'Вблизи'
    }

    descriptors = {
        'MI': 'Тонкий (поземный)',
        'BC': 'Обрывки, клочья',
        'PR': 'Частичный',
        'DR': 'Поземок',
        'BL': 'Низовая',
        'SH': 'Ливень (ливни)',
        'TS': 'Гроза',
        'FZ': 'Замерзающий'
    }

    precipitations = {
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

    bad_visibility_weather_events = {
        'BR': 'Дымка',
        'FG': 'Туман',
        'FU': 'Дым',
        'VA': 'Вулканический пепел',
        'DU': 'Пыль обложная',
        'SA': 'Песок',
        'HZ': 'Мгла',
    }

    other_weather_events = {
        'PO': 'Пыльные/песчаные вихри',
        'SQ': 'Шквалы',
        'FC': 'Воронкообразное(ые) облако(а) (торнадо или водяной смерч)',
        'SS': 'Песчаная буря',
        'DS': 'Пыльная буря'
    }

    RVR_prefixes = {
        'L': 'Левая',
        'C': 'Центральная',
        'R': 'Правая'
    }

    RVR_visibilty_prefixes = {
        'P': 'Длиннее чем 2000 метров',
        'M': 'Меньше минимального значения'
    }

    RVR_visibility_changements_prefixes = {
        'U': 'Увеличение видимости',
        'D': 'Уменьшение видимости',
        'N': 'Нет изменений в видимости'
    }

    RVR_deposits = {
        '0': 'Чисто и сухо',
        '1': 'Влажно',
        '2': 'Мокро',
        '3': 'Покрытая изморозью и инеем',
        '4': 'Иней изморозь',
        '5': 'Мокрый снег',
        '6': 'Слякоть',
        '7': 'Лёд',
        '8': 'Укатанный снег',
        '9': 'Мёрзлая неровная ВПП'
    }

    RVR_extends_of_contamination = {
        '1': '<10%',
        '2': '11-25%',
        '5': '26-51%',
        '9': '51-100%',
    }

    cloudiness = {
        "VV": "Состояние неба не определяется, например, не видно из-за тумана и/или других явлений",
        "FEW": "Несколько, 1-2 октанта",
        "SCT": "Разбросанные, 3-4 октанта",
        "BKN": "Значительные, 5-7 октантов",
        "OVC": "Сплошные, 8 октантов",
        "NSC": "Нет значимой для полетов облачности",
        "NCD": "Нет облачности; используется, когда автоматическая система не обнаружила облаков",
        "SKC": "Ясно",
        "CB": "Кучево-дождевые облака",
        "TCU": "Мощно-кучевые"
    }

    RVR_weathers = {
        'CLSD': 'ВПП закрыта',
        'CLRD': 'Чисто',
        'SNOKLO': 'ВПП закрыта снегом'
    }

    not_found_message = 'Не найдено! Напишите issue с фото)'

    value_error = "Неверный код аэропорта"
    internet_error = "Проверьте подключение к интернету и код аэропорта"

    Airport_code = 'Код аэропорта (icao)'
    Airport_name = 'Название аэропорта'
    Date_and_time = 'Дата и время'
    Wind_direction = 'Направление ветра'
    Wind_speed = 'Скорость ветра'
    Wind_gust = 'Порывы ветра'
    RVR = 'ВПП'
    Parallel = 'Параллельная'
    Visibility_prefix = 'Префикс видимости'
    Visibility_changes = 'Изменения видимости'
    Weather = 'Погода'
    RVR_deposit = 'Состояние полосы'
    Braking_friction_coefficient = 'Коэффициент сцепления'
    Intensivity = 'Интенсивность'
    Descriptor = 'Декскриптор'
    Precipitations = 'Осадки'
    Bad_visibility_weather_events = 'Плохая видимость из-за погодных явлений'
    Other_weather_events = 'Другие погодные явления'
    Cloudiness = 'Облачность'
    Height = 'Высота'
    Temperature = 'Температура'
    Dewpoint = 'Точка росы'
    Pressure = 'Давление'
    Name = 'Название'
    Value = 'Значение'
    Visibility = 'Видимость'
    Extend_of_contamination = 'Степень загрязнения'
    Depth_of_deposit = 'Отложения'
    Metar_decoder = 'Расшифровщик метара'
    Calculator_settings = 'Калькулятор + настройки'
    Language = 'Язык'
    Quickbar = 'Быстрая панель'
    Save_settings = 'Сохранить настройки'
    Trend = 'Прогноз'
    Time = 'Время'

    new_airport = 'Код аэропорта'
    new_airport_code = 'Новый код аэропорта'

    trends = {
        'NOSIG': 'Без изменений',
        'BECMG': 'Постепенно',
        'TEMPO': 'Временно',
        'NSW': 'Нет особых явлений погоды',
        'FM': 'Начало',
        'TL': 'Конец',
        'AT': 'Конкретно'
    }

    trend_time = {
        "FM": "От",
        "TL": "До",
        "AT": "В"
    }

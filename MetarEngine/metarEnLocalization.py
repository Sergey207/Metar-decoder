class EnLocale:
    intensivities = {
        '-': 'Light',
        '': 'Moderate',
        '+': 'Heavy',
        'VC': 'In the vicinity'
    }

    descriptors = {
        'MI': 'Shallow',
        'BC': 'Patches',
        'PR': 'Partial',
        'DR': 'Low drifting',
        'BL': 'Blowing',
        'SH': 'Shower',
        'TS': 'Thunderstorm',
        'FZ': 'Freezing'
    }

    precipitations = {
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

    bad_visibility_weather_events = {
        'BR': 'Mist',
        'FG': 'Fog',
        'FU': 'Smoke',
        'VA': 'Volcanic ash',
        'DU': 'Widespread dust',
        'SA': 'Sand',
        'HZ': 'Haze',
    }

    other_weather_events = {
        'PO': 'Dust/sand whirls',
        'SQ': 'Squalls',
        'FC': 'Funnel cloud(s) (tornado or water spout)',
        'SS': 'Sandstorm',
        'DS': 'Duststorm'
    }

    RVR_prefixes = {
        'L': 'Left',
        'C': 'Center',
        'R': 'Right'
    }

    RVR_visibilty_prefixes = {
        'P': 'Longer then 2000 m',
        'M': 'Shorter then minimal value'
    }

    RVR_visibility_changements_prefixes = {
        'U': 'Increase of visibility',
        'D': 'Decrease of visibility',
        'N': 'No changes of visibility'
    }

    RVR_deposits = {
        '0': 'dry and clear',
        '1': 'damp',
        '2': 'wet or water patches',
        '3': 'rime or frost',
        '4': 'dry snow',
        '5': 'wet snow',
        '6': 'slush',
        '7': 'ice',
        '8': 'compacled or rolled snow',
        '9': 'frozen ruls or ridges'
    }

    RVR_extends_of_contamination = {
        '1': '<10%',
        '2': '11-25%',
        '5': '26-51%',
        '9': '51-100%',
    }

    cloudiness = {
        "VV": "Vertical visibility",
        "FEW": "Few",
        "SCT": "Scallered",
        "BKN": "Broken",
        "OVC": "Overcast",
        "NSC": "No significant clouds",
        "NCD": "No clouds",
        "SKC": "Sky clear",
        "CB": "Сumulonimbus clouds",
        "TCU": "Lowering cumulus"
    }

    RVR_weathers = {
        'CLSD': 'RVR closed',
        'CLRD': 'RVR cleared',
        'SNOKLO': 'RVR snow closed'
    }

    not_found_message = 'Not found! Write issue with photos)'

    value_error = "Value Error -> Error airport code"
    internet_error = "Internet Error -> Check your internet connection or Airport code"

    Airport_code = 'Airport code (icao)'
    Airport_name = 'Aiport name'
    Date_and_time = 'Date and time'
    Wind_direction = 'Wind direction'
    Wind_speed = 'Wind speed'
    Wind_gust = 'Wind gust'
    RVR = 'RVR'
    Parallel = 'parallel'
    Visibility_prefix = 'visibility prefix'
    Visibility_changes = 'visibility changes'
    Weather = 'Weather'
    RVR_deposit = 'RVR deposit'
    Braking_friction_coefficient = 'braking friction coefficient'
    Intensivity = 'intensivity'
    Descriptor = 'descriptor'
    Precipitations = 'precipitations'
    Bad_visibility_weather_events = 'bad visibility weather events'
    Other_weather_events = 'other weather events'
    Cloudiness = 'Cloudiness'
    Height = 'Height'
    Temperature = 'Temperature'
    Dewpoint = 'Dewpoint'
    Pressure = 'Pressure'
    Name = 'Name'
    Value = 'Value'
    Visibility = 'Visibility'
    Extend_of_contamination = 'extend of contamination'
    Depth_of_deposit = 'depth of deposit'
    Metar_decoder = 'Metar decoder'
    Calculator_settings = 'Calculator + settings'
    Language = 'Language'
    Quickbar = 'Quickbar'
    Save_settings = 'Save settings'
    Trend = 'Trend'
    Time = 'Time'
    TAF = 'TAF'
    Action_time = 'Action time'
    Air_temperature = 'Air temperature'
    Min = 'Minimum'
    Max = 'Maximum'
    Day = 'Day'
    Duration = 'Duration'

    new_airport = 'Airport code'
    new_airport_code = 'New airport code'

    trends = {
        'NOSIG': 'No significant change',
        'BECMG': 'Becoming',
        'TEMPO': 'Temporary',
        'NSW': 'No significant weather',
        'FM': 'From',
        'TL': 'Till',
        'AT': 'At'
    }

    trend_time = {
        "FM": "From",
        "TL": "To",
        "AT": "At"
    }

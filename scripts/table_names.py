import json

table_names = {
    'PA': 'AIRPORT',
    'PS': 'AIRPORT_MSA',
    'PB': 'AIRPORT_GATE',
    'UC': 'CONTROLLED_AIRSPACE',
    'ER': 'ENROUTE_AIRWAYS',
    'UF': 'FIR_UIR',
    'EP': 'HOLDING_PATTERN',
    'PI': 'LOCALIZER',
    'PM': 'LOCALIZER_MARKER',
    'DB': 'NDB_NAVAID',
    'PN': 'NDB_NAVAID',
    'UR': 'RESTRICTIVE_AIRSPACE',
    'PG': 'RUNWAY',
    'PD': 'SID_STAR_APPROACH',
    'PE': 'SID_STAR_APPROACH',
    'PF': 'SID_STAR_APPROACH',
    'D': 'VHF_NAVAID',
    'EA': 'WAYPOINT',
    'PC': 'WAYPOINT',
    'PV': 'AIRPORT_COMMUNICATIONS',
    'EV': 'ENROUTE_COMMUNICATIONS',
}

mapping = dict()

def update_cont(desc, cont):
    res = [None, None]

    for record in cont:
        if record['format_code'] is not None:
            format_code = int(record['format_code'])
            pos = int(record['min_pos'])

            if format_code == 4:
                res[0] = pos
            elif format_code == 5:
                res[1] = pos

            if (res[0] is not None) and (res[1] is not None):
                break

    key = tuple(res)
    if not(key in mapping):
        mapping[key] = [desc]
    else:
        mapping[key] += desc


def parse_info(info):
    for record_id, record in info.iteritems():
        for cont_id, cont in record['conts'].iteritems():
            if (cont_id == '1'):
                update_cont(tuple(record['codes']),  cont)


with open('dump.txt', 'rt') as f:
    info = json.loads(f.read())

parse_info(info)

for key, value in mapping.iteritems():
    print key, ':', value

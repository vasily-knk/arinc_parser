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



with open('dump.txt', 'rt') as f:
    info = json.loads(f.read())

mapping = dict()

for record_id, record in info.iteritems():
    for code in record['codes']:
        table_name = table_names.get(code, '--undefined--')
        mapping[int(record_id)] = (code, table_name, record['description'])


for key, value in mapping.iteritems():
    print key, ':', value[0], ', ', value[1], ', ', value[2]

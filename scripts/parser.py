import re
import os
import json

from arinc_types import FieldDesc, RecordDesc, ArincJsonEncoder

records_codes = {
    1: ('', []),
    2: ('VHF NAVAID', ['D']),
    3: ('NDB NAVAID', ['DB', 'PN']),
    4: ('Waypoint', ['EA', 'PC']),
    5: ('Holding Pattern', ['EP']),
    6: ('Enroute Airways', ['ER']),
    7: ('Airport', ['PA']),
    8: ('Airport Gate', ['PB']),
    9: ('Airport SID/STAR/Approach', ['PD', 'PE', 'PF']),
    10: ('Runway', ['PG']),
    11: ('Airport and Heliport Localizer and Glide Slope', ['PI']),
    12: ('Company Route', ['R']),
    13: ('Airport and Heliport Localizer Marker', ['PM']),
    14: ('Airport Communications', ['PV']),
    15: ('Airways Marker', ['EM']),
    16: ('Cruising Tables', ['TC']),
    17: ('FIR/UIR', ['UF']),
    18: ('Restrictive Airspace', ['UR']),
    19: ('Grid MORA', ['AS']),
    20: ('Airport MSA', ['PS']),
    21: ('Enroute Airways Restrictive', ['EU']),
    22: ('Airport and Heliport MLS', ['PL']),
    23: ('Enroute Communications', ['EV']),
    24: ('Preferred Routes', ['ET']),
    25: ('Controlled Airspace', ['UC']),
    26: ('Geographical Reference Table', ['TG']),
    27: ('Flight Planning Arrival/Departure Data', ['PR']),
    28: ('Path Point', ['PP']),
    29: ('GLS', ['PT']),
    30: ('Alternate', ['RA']),
}


class FileParser:
    def __init__(self, record_id):
        self.__record_id = record_id
        self.__records_desc = RecordDesc(records_codes[record_id][1], records_codes[record_id][0], dict())

        self.__cont_id = None

    def __parse_empty(self, m):
        pass

    def __parse_section(self, m):
        cont_id = int(m.group(1))
        self.__cont_id = cont_id

    def __parse_record(self, m):
        min_pos = int(m.group(1))
        max_pos = min_pos if m.group(2) is None else int(m.group(2))
        description = m.group(3)
        format_code = None if m.group(4) is None else int(m.group(4))
        field = FieldDesc(min_pos, max_pos, description, format_code)

        if not (self.__cont_id in self.__records_desc.conts):
            self.__records_desc.conts[self.__cont_id] = []

        self.__records_desc.conts[self.__cont_id].append(field)

    def parse_line(self, line):
        matchers = [
            (r'(\d+)(?: thru (\d+))?' + r'\t' + r'([^\t]+)' + r'\t' + r'(?:5\.(\d+))?(?: Note \d)?|Note \d', self.__parse_record),
            (r'\[(\d+)\]', self.__parse_section),
            (r'', self.__parse_empty),
        ]

        pre = r'^\s*'
        suf = r'\s*$'

        m = None
        for matcher in matchers:
            m = re.match(pre + matcher[0] + suf, line)
            if not(m is None):
                matcher[1](m)
                break

        if m is None:
            raise Exception('Can\'t parse ' + line)

    def get_data(self):
        return self.__records_desc


def parse_file(record_id, file_path):
    parser = FileParser(record_id)
    with open(file_path, 'rt') as f:
        lines = f.readlines()

        for line in lines:
            parser.parse_line(line.strip('\n'))

    return parser.get_data()


if __name__ == '__main__':
    location = '../desc/'
    info = dict()

    for i in xrange(1, 31):
        if i in info:
            raise Exception(str(i) + ' already defined')
        filename = str(i).zfill(2)
        print 'File', filename
        path = os.path.join(location, filename)
        info[i] = parse_file(i, path)

    with open('dump.txt', 'wt') as out_file:
        out_file.write(json.dumps(info, cls=ArincJsonEncoder, sort_keys=True, indent=4, separators=(',', ': ')))

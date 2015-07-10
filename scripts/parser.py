import re
import os
import json

class AutoJSONable:
    pass

class FieldDesc(AutoJSONable):
    def __init__(self, min_pos, max_pos, description, format_code):
        self.min_pos = min_pos
        self.max_pos = max_pos
        self.description = description
        self.format_code = format_code

class MyJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, AutoJSONable):
            return o.__dict__
        return json.JSONEncoder.default(self, o)



class FileParser:
    def __init__(self, record_id):
        self.__record_id = record_id
        self.__cont_id = None
        self.__data = dict()

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

        if not (self.__cont_id in self.__data):
            self.__data[self.__cont_id] = []

        self.__data[self.__cont_id].append(field)

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
        return self.__data


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
        out_file.write(json.dumps(info, cls=MyJsonEncoder, sort_keys=True, indent=4, separators=(',', ': ')))

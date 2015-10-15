import json
from operator import itemgetter

stats = dict()


with open('arinc_format.json', 'rt') as f:
    info = json.loads(f.read())

def record_type_by_code(code):
    for record_id, record in info['airlines'].iteritems():
        if code in record['codes']:
            return record_id
    return None


def get_code(line):
    code = line[4:6]
    if code == 'P ':
        code = 'P' + line[12]
    return code

def find_first_type


def process_file(filename)
    with open(filename, 'rt') as f:
        for l in f:
            line = l.strip('\n')
            if not(line[0] in ['S', 'T']):
                continue
            code = get_code(line)
            record_type = record_type_by_code(code)
            cont_pos = info['airlines'][record_type]["1"]


process_file(r'C:\work\arinc\BD_2014-11-13_400000995211295')
mapping = dict()

"""
 for record_id, record in info['airlines'].iteritems():
    for code in record['codes']:
        mapping[code] = (int(record_id), record['description'])

records_in_arinc = sorted(stats.items(), key=itemgetter(1), reverse=True)

for code, count in records_in_arinc:
    lookup_code = code.rstrip()
    desc = mapping.get(lookup_code, (0, '--undefined--'))
    print code, ': ', desc, ': ', count
"""
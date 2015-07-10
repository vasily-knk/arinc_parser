import json
from operator import itemgetter

stats = dict()

with open('../arinc_adacel.TXT', 'rt') as f:
    for l in f:
        line = l.strip('\n')
        if not(line[0] in ['S', 'T']):
            continue

        code = line[4:6]
        if code[1] == ' ':
            code = code[0]

        if not(code in stats):
            stats[code] = 1
        else:
            stats[code] += 1


with open('dump.txt', 'rt') as f:
    info = json.loads(f.read())

mapping = dict()

for record_id, record in info.iteritems():
    for code in record['codes']:
        mapping[code] = (int(record_id), record['description'])

records_in_arinc = sorted(stats.items(), key=itemgetter(1), reverse=True)

for code, count in records_in_arinc:
    desc = mapping.get(code, (0, '--undefined--'))
    print code, ':', count, desc[1]
import json
from operator import itemgetter

def convert_name(name):


with open('arinc_format.json', 'rt') as f:
    info = json.loads(f.read())

stats = dict()

for record_id, record in info['airlines'].iteritems():
    for cont, fields in record['conts'].iteritems():
        for field in fields:
            name = field['description']
            if not(name in stats):
                stats[name] = 1
            else:
                stats[name] += 1


sorted_names = sorted(stats.items(), key=itemgetter(1), reverse=True)

for name, count in sorted_names:
    print name, count


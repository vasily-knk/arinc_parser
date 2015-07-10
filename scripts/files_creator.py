num_types = 30
max_subtypes = 10

for type_id in xrange(1, num_types + 1):
    filename = str(type_id).zfill(2)
    with open(filename, 'wt') as f:
        for subtype_id in xrange(1, max_subtypes + 1):
            f.write('[' + str(subtype_id) + ']\n\n')

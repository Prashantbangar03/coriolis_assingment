def numbered_file(filepath):
    file_in = open(filepath)
    file_out = open('pallindrom_version.py', 'w')
    for line, content in enumerate(file_in):
        file_out.write('%s %s' % (line + 1, content))



numbered_file('pallindrom_version.py')

#!/usr/bin/python
#author james@smackagency.com
import sys
import json
import io
import string

def main(argv):
    try:
        with io.open('version.json', encoding='utf-8') as data_file:
            current_version = json.loads(data_file.read())

        exploded_current = current_version['version'].split(",")

        x = 0
        for number in exploded_current:
            exploded_current[x] = int(number)
            x += 1

        if sys.argv[1] == "major":
            exploded_current[0] = int(exploded_current[0]) + 1
            print 'Major update'

        elif sys.argv[1] == "minor":
            exploded_current[1] = int(exploded_current[1]) + 1
            print 'Minor update'

        elif sys.argv[1] == "hotfix":
            exploded_current[2] = int(exploded_current[2]) + 1
            print 'Bug fix'

        else:
            print 'Have not defined a known update kind'

    except:
        print 'Could not open version.json'

    new_version = ','.join([unicode(i) for i in exploded_current])

    try:
        with open('version.json','w') as outfile:
            json.dump({'version':new_version}, outfile)

    except:
        print 'Could not write new file'

if __name__ == "__main__":
    main(sys.argv[1:])
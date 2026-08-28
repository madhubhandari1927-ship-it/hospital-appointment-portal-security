#!/usr/bin/env python3
import sys
import json


def get_vulnerabilities(name, db):
        data = json.load(db)

        if name not in data:
                return []

        vulnerabilities = []

        for vulnerability in data[name]:
                vulnerability_id = vulnerability.get('id')
                version = vulnerability.get('v')
                cve = vulnerability.get('cve')

                vulnerabilities.append(
                        (vulnerability_id, version, cve)
                )

        return vulnerabilities


def main(argv):
        name = argv[1]
        db = open(argv[2])

        vulnerabilities = get_vulnerabilities(name, db)

        for v in vulnerabilities:
                print('%s; %s; %s' % (v[0], v[1], v[2]))


# This makes sure the main function is not called immediately
# when TMC imports this module
if __name__ == "__main__":
        if len(sys.argv) != 3:
                print('usage: python %s name db' % argv[0])
        else:
                main(sys.argv)
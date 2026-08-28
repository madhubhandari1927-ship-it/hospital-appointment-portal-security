#!/usr/bin/env python3

import sys
import sqlite3


def read_database(conn):
    agents = []

    cursor = conn.execute(
        "SELECT id, name FROM Agent ORDER BY id"
    )

    for row in cursor:
        agents.append((row[0], row[1]))

    return agents


def main(argv):
    name = argv[1]

    conn = sqlite3.connect(name)

    agents = read_database(conn)

    for agent in agents:
        print(agent[0], agent[1])

    conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python %s database" % sys.argv[0])
    else:
        main(sys.argv)
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


def add_agent(conn, aid, name):
    conn.execute(
        "INSERT INTO Agent (id, name) VALUES (?, ?)",
        (aid, name)
    )
    conn.commit()


def delete_agent(conn, aid):
    conn.execute(
        "DELETE FROM Agent WHERE id = ?",
        (aid,)
    )
    conn.commit()


def main(argv):
    database = argv[1]
    conn = sqlite3.connect(database)

    while True:
        agents = read_database(conn)

        print("Active agents:")
        print()

        for agent in agents:
            print(agent[0], "\t", agent[1])

        print()

        choice = input(
            "What would you like to do: [a]dd, [r]emove, or [q]uit? "
        )

        if choice == "a":
            aid = input("id? ")
            name = input("name? ")
            add_agent(conn, aid, name)

        elif choice == "r":
            aid = input("id? ")
            delete_agent(conn, aid)

        elif choice == "q":
            break

    conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python %s database" % sys.argv[0])
    else:
        main(sys.argv)
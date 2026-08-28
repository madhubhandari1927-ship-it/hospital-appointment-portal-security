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


def add_agent(conn, agent_id, name):
    conn.execute(
        "INSERT INTO Agent (id, name) VALUES (?, ?)",
        (agent_id, name)
    )
    conn.commit()


def remove_agent(conn, agent_id):
    conn.execute(
        "DELETE FROM Agent WHERE id = ?",
        (agent_id,)
    )
    conn.commit()


def print_agents(conn):
    agents = read_database(conn)

    print("Active agents:")
    print()

    for agent in agents:
        print(agent[0], "\t", agent[1])

    print()


def main(argv):
    database = argv[1]

    conn = sqlite3.connect(database)

    while True:
        print_agents(conn)

        choice = input(
            "What would you like to do: [a]dd, [r]emove, or [q]uit? "
        )

        if choice == "a":
            agent_id = input("id? ")
            name = input("name? ")

            add_agent(conn, agent_id, name)

        elif choice == "r":
            agent_id = input("id? ")

            remove_agent(conn, agent_id)

        elif choice == "q":
            break

    conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python %s database" % sys.argv[0])
    else:
        main(sys.argv)
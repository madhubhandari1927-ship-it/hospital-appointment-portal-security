def read_database(conn):
    agents = []

    cursor = conn.execute(
        "SELECT id, name FROM Agent ORDER BY id"
    )

    for row in cursor:
        agents.append((row[0], row[1]))

    return agents
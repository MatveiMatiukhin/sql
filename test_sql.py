import psycopg2
from projects.sql.config import host, user, password, db_name


try:
    pass
    connection = psycopg2.connect(
        host=host, user=user, password=password, database=db_name
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute("""SELECT version()""")
        print(f"Server version: {cursor.fetchone()}")

    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO users (id, first_name, second_name, email)
            VALUES (4, 'tui', 'tuio', 'lp');"""
        )
        print(f"[INFO] {cursor.fetchone()}")


except Exception as _ex:
    print("[INFO] Error while working with POstreSQl")
finally:
    if connection:
        connection.close()
        print("[INFO] connection closed")

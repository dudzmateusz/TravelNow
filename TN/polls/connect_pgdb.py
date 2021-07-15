from psycopg2 import connect, Error

try:
    # declare a new PostgreSQL connection object
    conn = connect(
        dbname = "TN",
        user = "postgres",
        host = "127.0.0.1",
        password = "polpol",
        # attempt to connect for 3 seconds then raise exception
        connect_timeout = 4
    )

    cur = conn.cursor()
    print ("\ncreated cursor object:", cur)

except (Exception, Error) as err:
    print ("\npsycopg2 connect error:", err)
    conn = None
    cur = None
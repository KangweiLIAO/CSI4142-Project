import psycopg2
import os
from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    filename = os.getcwd() + "/scripts/" + filename
    # create a parser
    parser = ConfigParser()
    # read config file

    if os.path.isfile(filename):
        parser.read(filename)
    else:
        print("Database config file not found!")
        return None

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
        if (params == None):
            return

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        query = str(input("Enter a SQL Query: "))
        print()
        cur.execute(query)

        # display the PostgreSQL database server version
        db_respond = cur.fetchone()
        print(db_respond)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()

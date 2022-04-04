import os
import psycopg2
import sqlalchemy
from configparser import ConfigParser

pg_info = {}
pg_conn = None
sql_engine: sqlalchemy.engine = None


def config_database(filename='database.ini', section='postgresql'):
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
    global pg_info
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            pg_info[param[0]] = param[1]
    else:
        raise Exception(f"Section {section} not found in the {filename} file")


def connect():
    """ Connect to the PostgreSQL database server """
    global pg_conn, sql_engine
    try:
        # read connection parameters
        config_database()
        if (pg_info == None):
            return

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        sql_engine = sqlalchemy.create_engine(
            f"postgresql://{pg_info['user']}:{pg_info['password']}@{pg_info['host']}:{pg_info['port']}/{pg_info['database']}").connect()
        pg_conn = psycopg2.connect(**pg_info)
        pg_conn.autocommit = True
        print('Connection established.')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def execute_sql(query: str, fetch: bool = False):
    if (not pg_conn):
        return
    try:
        # create a db cursor
        cur = pg_conn.cursor()
        # execute a statement
        cur.execute(query)
        if(fetch):
            resp = cur.fetchall()
            return resp
    except Exception as error:
        print(error)
    finally:
        cur.close()


def grant_permit(tables, user: str = "lzou041"):
    if (tables):
        for table in tables:
            execute_sql(f"GRANT ALL ON public.{table} TO {user};")
    else:
        print(f"No table selected to grant to {user}...")


def disconnect():
    if pg_conn is not None:
        pg_conn.close()
        print('Database connection closed.')
    if sql_engine is not None:
        sql_engine.close()
        print('SQL engine connection closed.')

import psycopg2
from psycopg2 import Error
from config import host, user, password, db_name
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def create_connection():
    global connection
    try:
        connection = psycopg2.connect(host=host, user=user,
                                      password=password, database=db_name)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        cursor.execute(
            "SELECT table_name FROM information_schema.tables where table_schema = 'public' ORDER BY table_name")
        print(cursor.fetchall())
        print("Connection to PostgreSQL DB successful")
    except Error as db_connection_error:
        print("Error", db_connection_error)

    return connection


def create_group():
    global connection
    try:
        connection = psycopg2.connect(host=host, user=user,
                                      password=password, database=db_name)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO auth_group(id, name) VALUES(8,'group_1')")
        connection.commit()
        print("Group is created successful")
    except Error as db_create_group:
        print("Error", db_create_group)

    return connection


def create_user():
    global connection
    try:
        connection = psycopg2.connect(host=host, user=user,
                                      password=password, database=db_name)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO auth_user(username, email, password, first_name,last_name, is_staff, "
                       "is_superuser, is_active, date_joined) VALUES ('user_1', 'www.user_1@gmail.com', 1234, 'user', "
                       "'user', True, True, False, '2-19-2021')")
        connection.commit()
        print("User is created successful")
    except Error as db_create_user:
        print("Error", db_create_user)


def add_user_in_group():
    global connection
    try:
        connection = psycopg2.connect(host=host, user=user,
                                      password=password, database=db_name)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM auth_group as g "
                       "LEFT JOIN auth_user_groups ug on g.id = ug.group_id "
                       "LEFT JOIN auth_user u on ug.user_id = u.id "
                       "WHERE u.username = 'user_1' ")
        connection.commit()
        print("User add in group succesfully")
    except Error as db_adding_error:
        print("Error", db_adding_error)


print(create_connection())
print(create_group())
print(create_user())
cursor.close()
connection.close()

# Team Big Fit
# Created by: Serena Villacorta
# Big Fit Data Access Object

import sqlite3 as lite
from sqlite3 import Error
import os


class BigFitDAO(object):
    os.chdir(os.path.dirname(__file__))
    __path = os.path.join(os.getcwd(), "BigFitDB")
    __select_users_SQL = 'select user_id, first_name, last_name, start_weight, target_weight, feet, inches' \
                         ', date_of_birth, gender, zip_code, email, start_date, end_date, password from bf_user'
    __insert_user_SQL = 'insert into bf_user (first_name,last_name, start_weight, target_weight, feet, inches, ' \
                        'date_of_birth, gender, zip_code, email, start_date, end_date, password) ' \
                        'values(?,?,?,?,?,?,?,?,?,?,?,?,?)'

    @staticmethod
    def create_connection():
        try:
            conn = lite.connect(BigFitDAO.__path)
            return conn
        except Error as e:
            print(e)
        return None

    @staticmethod
    def select_all_users(conn):
        cur = conn.cursor()
        cur.execute(BigFitDAO.__select_users_SQL)
        rows = cur.fetchall()
        return rows

    @staticmethod
    def select_user_by_user_id(conn, user_id):
        cur = conn.cursor()
        cur.execute("SELECT * FROM bf_user WHERE user_id=?", (user_id,))
        rows = cur.fetchall()
        return rows

    @staticmethod
    def insert_user(conn, user):
        cur = conn.cursor()
        user_tuple = (user.last_name, user.first_name, user.start_weight, user.target_weight, user.feet, user.inches,
                        user.date_of_birth, user.gender, user.zip_code, user.email, user.start_date, user.end_date,
                        user.password)

        cur.execute(BigFitDAO.__insert_user_SQL, user_tuple)
        conn.commit()



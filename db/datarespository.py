# Main.Repository.datarespository.py

import sqlite3

import pandas as pd


class Datarepository:

    def __init__(self, databasename):
        self.__databasename = databasename

    def add_entry(self, entry):
        query = """insert into weather_data (location, timestamp, temperature, sunshine, precipation, pressure, wind_gust)
                 values (?, ?, ?, ?, ?, ?, ?)"""
        # print(entry)
        # params = (entry['location'], entry['timestamp'], entry['temperature'], entry['sunshine'], entry['precipation'])
        # params = params + (entry['pressure'], entry['wind_gust'],)
        # self.__edit_query(query, params)

    def __edit_query(self, query, params):
        connection = self.__database_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()
        except Exception as e:
            print('error', e)
        finally:
            connection.close()

    def __database_connection(self):
        try:
            return sqlite3.connect(self.__databasename)
        except Exception as e:
            print(f'not plausible to connect to database {self.__databasename}')
            print('Due to error: ', e)
            exit(-1)

    def add_entry_from_df(self, df):
        connection = self.__database_connection()
        df.to_sql(name='weather_data', con=connection, if_exists='replace', index=False)

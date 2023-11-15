# Main.Repository.datarespository.py

import sqlite3

import pandas as pd


class Datarepository:

    def __init__(self, databasename):
        self.__databasename = databasename

    def get_data_by_location_name(self, location_name):
        query = '''select weather_data.* from 
                weather_data inner join location l on l.id = weather_data.location where 
                l.location_name is ?'''
        return pd.read_sql_query(query, self.__database_connection(), params=(location_name,))

    def get_all_rainfall(self):
        query = '''select weather_data.timestamp, weather_data.precipation, l.location_name from 
            weather_data inner join location l on l.id = weather_data.location'''
        return pd.read_sql_query(query, self.__database_connection())

    def add_entry_from_df(self, df):
        connection = self.__database_connection()
        df.to_sql(name='weather_data', con=connection, if_exists='replace', index=False)

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
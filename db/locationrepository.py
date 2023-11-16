# Main.Repository.locationrepository.py

from dotenv import load_dotenv

import sqlite3
import os


class Locationrepository:

    def __init__(self):
        load_dotenv()
        self.__databasename = self.__databasename = os.environ.get('DATABASE_PATH')

    def get_location_by_name(self, location_name):
        query = "select * from location where location.location_name is ?"

        result = self.__fetch_one(query, location_name)

        return result

    def add_location(self, location):
        query = "select count (*) from location"

        result = self.__fetch_query(query)

        if result is None:
            result = 0
        else:
            result += result

        query = '''
            insert into location (id, location_name, lat, lon, asl, resolution, aggregation)
            values (?, ?, ?, ?, ?, ?, ?)
        '''

        params = (result, location['location'], location['lat'], location['lon'], location['asl'])
        params = params + (location['resolution'], location['aggregation'],)
        self.__edit_query(query, params)

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

    def __fetch_query(self, query):
        connection = self.__database_connection()
        result = None
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchone()[0]
        except Exception as e:
            print('error', e)

        finally:
            connection.close()
        return result

    def __fetch_one(self, query, params):
        connection = self.__database_connection()
        result = None
        try:
            cursor = connection.cursor()
            cursor.execute(query, (params,))
            result = cursor.fetchone()
        except Exception as e:
            print('error', e)

        finally:
            connection.close()
        return result

    def __database_connection(self):
        try:
            return sqlite3.connect(self.__databasename)
        except Exception as e:
            print(f'not plausible to connect to database {self.__databasename}')
            print('Due to error: ', e)

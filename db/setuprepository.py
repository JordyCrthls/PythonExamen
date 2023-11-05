# setup.repo.py

import sqlite3


class Repo:

    def __init__(self, databasename):
        self.__databasename = databasename
        self.init_database()

    def init_database(self):
        self.create_database()

    def create_database(self):
        query = """
            create table if not exists location (
                id integer primary key,
                location_name text,
                lat double,
                lon double,
                asl varchar(10),
                level varchar(20),
                resolution varchar(10),
                aggregation varchar(255)
            );
        """
        self.__database_connection().cursor().execute(query)
        query = """
            create table if not exists weather_data (
                location integer,
                timestamp datetime,
                temperature double,
                sunshine double,
                precipation double,
                pressure double,
                wind_gust double,
                PRIMARY KEY (location, timestamp)
                foreign key(location) references location(id)
            );
            """
        self.__database_connection().cursor().execute(query)

    def __database_connection(self):
        try:
            return sqlite3.connect(self.__databasename)
        except Exception as e:
            print(f'not plausible to connect to database {self.__databasename}')
            print('Due to error: ', e)
            exit(-1)

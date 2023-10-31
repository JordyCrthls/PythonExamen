#repo.py

import sqlite3, os

class Repo:

	def __init__(self, databasename="corthalsjordy.db"):
		self.__databasename = databasename
		try:
			self.__connection = sqlite3.connect(self.__databasename)
		except Exception as e:
			print(f'not plausible to connect to database {__databasename}')
			print('Due to error: ', e)
			exit(-1)
		self.init_database(databasename)

	def get_new_id(self):
		query = "count(*) from locations"

	def init_database(self, databasename):
		self.create_database(databasename)

	def create_database(self, databasename):
		query = f"""
			create table location (
    			id integer primary key,
    			location text,
    			lat double,
    			lon double,
    			asl varchar(10),
    			level varchar(20),
    			resolution varchar(10),
    			aggregation varchar(255)
	
			);
		"""
		self.__connection.cursor().execute(query)
		query = """
			create table weather_data (
    			id integer primary key,
    			location integer,
    			foreign key(location) references location(id)
			);
			"""
		self.__connection.cursor().execute(query)


#setup.repo.py

import sqlite3, os, sys

from Main.Repository.mainrepository import DatabaseConnection

class Repo:

	def __init__(self, connection):
		self.__connection = connection
		self.init_database()

	def init_database(self):
		self.create_database()

	def create_database(self):
		query = f"""
			create table if not exists location (
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
		self.__connection.get_connection().cursor().execute(query)
		query = """
			create table if not exists weather_data (
    			id integer primary key,
    			location integer,
    			foreign key(location) references location(id)
			);
			"""
		self.__connection.get_connection().cursor().execute(query)


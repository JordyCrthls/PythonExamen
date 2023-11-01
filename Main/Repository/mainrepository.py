#Main.Repository.mainrepository.py

import sqlite3

class DatabaseConnection:

	def __init__(self, databasename):
		self.__databasename = databasename
		try:
			self.__connection = sqlite3.connect(self.__databasename)
		except Exception as e:
			print(f'not plausible to connect to database {databasename}')
			print('Due to error: ', e)
			exit(-1)

	def get_connection(self):
		return self.__connection
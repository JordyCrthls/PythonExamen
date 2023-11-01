#Setup.setup.py

import pandas as pd
import sys, csv, os
from Setup.setuprepository import Repo
from Main.Repository.mainrepository import DatabaseConnection
from Main.Repository.locationrepository import Locationrepository

class Setup:

	def __init__(self, databasename, src):
		self.__databasename = databasename
		self.__src_file = src
		db_connection = DatabaseConnection(self.__databasename)
		self.__repo = Repo(db_connection)
		self.__locationrepo = Locationrepository(db_connection)

		
	def set_src(self, src):
		if(src != None and src.strip() != ''):
			self.__src_file = src

	def instanciate(self, databasename=None, filename=None):
		self.set_src(filename)
		if(self.__databasename == None):
			raise Exception('Er kan niet geconnecteerd worden met de database, geef een naam op via het \'set_database\' commando')
		self.fill_db()

	def fill_db(self):
		if(self.__src_file == None):
			raise Exception('Er is geen csv bestandsnaam opgegeven, geef de naam op via het \'set_src\' commando')
		cleaned_data = self.cleaning_data()

	def cleaning_data(self):
		path = os.getcwd()
		file_path = os.path.join(path, self.__src_file)
		try:
			with open(file_path, 'r') as input_file:
				reader = list(csv.reader(input_file, delimiter=","))
				metadata = reader[:9]
				cleaned_up = reader[9:]
		except Exception as e:
			print('faild to open file due to ', e)
			exit(-1)
		return (metadata, cleaned_up)
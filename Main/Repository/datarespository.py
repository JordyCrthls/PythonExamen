#Main.Repository.datarespository.py

import sqlite3
from Main.Repository.mainrepository import DatabaseConnection

class Datarepository(Repository):

	def __init__(self, connection):
		self.__connection = connection
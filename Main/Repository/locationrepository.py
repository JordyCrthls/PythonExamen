#Main.Repository.locationrepository.py

import sqlite3
from Main.Repository.mainrepository import DatabaseConnection

class Locationrepository:

	def __init__(self, connection):
		self.__connection = connection

	def get_new_id(self):
		query = "count(*) from locations"

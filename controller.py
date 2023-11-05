#controller.py

import sys
from domain.setupdomain import SetupDomain
from domain.data import DataDomain

script_name, command = sys.argv

if len(sys.argv) != 2:
	print("Geef minimaal 2 argument op.")

database_name = input("Geef de database naam op of druk op enter voor de standaar database naam.")
if database_name is None or database_name.strip() == '':
	database_name = "corthalsjordy.db"
csv = "src.csv"
setup = SetupDomain(database_name, csv)
data_domain = DataDomain(database_name)

match command:
	case 'init':
		csv = input("Geef een csv bestand op, of druk op enter voor het standaard bestand.")
		setup.set_src(csv)
		setup.instantiate()
	case 'set_src':
		csv = input("Geef een csv bestand op, of druk op enter voor het standaard bestand.")
		setup.set_src(csv)
	case 'data-info':
		location_name = input('geef de naam van de gewenste locatie op, of druk op enter voor Basel.')
		if location_name == None or location_name == '':
			location_name = 'Basel'
		data_domain.get_info(location_name)

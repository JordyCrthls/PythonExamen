#controller.py

import sys
from Setup.setup import Setup

script_name, command = sys.argv

if len(sys.argv) != 2:
	print("Geef minimaal 2 argument op.")

databasename = input("Geef de database naam op of druk op enter voor de standaar database naam.")
if databasename is None or databasename.strip() == '':
	databasename = "corthalsjordy.db"
csv = "src.csv"
setup = Setup(databasename, csv)

match command:
	case 'init':
		csv = input("Geef een csv bestand op, of druk op enter voor het standaard bestand.")
		setup.set_src(csv)
		setup.instanciate()
	case 'set_src':
		csv = input("Geef een csv bestand op, of druk op enter voor het standaard bestand.")
		setup.set_src(csv)
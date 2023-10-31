#setup.py

import pandas as pd
import sys, csv
from repo import Repo


if len(sys.argv) != 2:
	print("Geef als argument een csv bestand op.")
	sys.exit(-1)

script_name, csv_file = sys.argv

#cleaning up
try:
	with open(csv_file, 'r') as input_file:
		reader = list(csv.reader(input_file, delimiter=","))
		metadata = reader[:9]
		cleaned_up = reader[9:]
except Exception as e:
	print('faild to open file due to ', e)
	exit(-1)


dataframe = pd.DataFrame(cleaned_up)
dataframemeta = pd.DataFrame(metadata)

repo = Repo()
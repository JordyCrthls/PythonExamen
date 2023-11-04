# Setup.setup.py

import csv
import os

import numpy as np

from db.setuprepository import Repo
from db.locationrepository import Locationrepository


class Setup:

    def __init__(self, databasename, src):
        self.__database_name = databasename
        self.__src_file = src
        self.__repo = Repo(databasename)
        self.__location_repo = Locationrepository(databasename)

    def set_src(self, src):
        if src is not None and src.strip() != '':
            self.__src_file = src

    def instantiate(self, filename=None):
        self.set_src(filename)
        self.__fill_db()

    def __fill_db(self):
        if self.__src_file is None:
            raise Exception('Er is geen csv bestandsnaam opgegeven, geef de naam op via het \'set_src\' commando')
        metadata, cleaned_up = self.__cleaning_data()
        location = self.__location_repo.get_location_by_name(metadata['location'])
        if location is None:
            self.__location_repo.add_location(metadata)
        else:
            print()


    def __add_data(self, data, location_id):
        print(location_id)

    def __cleaning_data(self):
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

        filtered_meta = []
        for sublist in metadata:
            filter_sub = []
            for item in sublist:
                if item not in filter_sub:
                    filter_sub.append(item)
            filtered_meta.append(filter_sub)
        metadata = [f for f in filtered_meta if len(f) == 2]

        meta_dictionary = {meta[0]: meta[1] for meta in metadata}
        return meta_dictionary, cleaned_up

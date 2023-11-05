# Setup.setup.py

import csv
import os

import pandas as pd

from db.setuprepository import Repo
from domain.location import LocationDomain
from domain.data import DataDomain


class SetupDomain:

    def __init__(self, databasename, src):
        self.__database_name = databasename
        self.__src_file = src
        self.__repo = Repo(databasename)
        self.__location_domain = LocationDomain(databasename)
        self.__data_domain = DataDomain(databasename)

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
        location = self.__location_domain.get_location_by_name(metadata['location'])
        if location is None:
            self.__location_domain.add_location(metadata)

        location = self.__location_domain.get_location_by_name(metadata['location'])
        self.__add_data(cleaned_up, location[0])

    def __add_data(self, data, location_id):
        df = pd.DataFrame(data)
        df['location'] = int(location_id)
        self.__data_domain.add_entry_from_df(df)

    def __cleaning_data(self):
        path = os.getcwd()
        file_path = os.path.join(path, self.__src_file)
        try:
            with open(file_path, 'r') as input_file:
                reader = list(csv.reader(input_file, delimiter=","))
                metadata = reader[:9]
                clean_data = reader[10:]
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

        clean_data = self.__transform_data(clean_data)

        meta_dictionary = {meta[0]: meta[1] for meta in metadata}
        return meta_dictionary, clean_data

    def __transform_data(self, data):
        df = pd.DataFrame(data)
        df.columns = ["timestamp", "temperature", "sunshine", "precipation", "pressure", "wind_gust"]
        df["temperature"] = df["temperature"].astype(float)
        df["sunshine"] = df["sunshine"].astype(float)
        df["precipation"] = df["precipation"].astype(float)
        df["pressure"] = df["pressure"].astype(float)
        df["wind_gust"] = df["wind_gust"].astype(float)
        df["timestamp"] = pd.to_datetime(df["timestamp"], format="%Y%m%dT%H%M%S")
        return df

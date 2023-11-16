# domain.setupdomain.py

import matplotlib.pyplot as plt
import pandas as pd

import os

from db.datarespository import Datarepository


class DataDomain:
    def __init__(self):
        self.__data_repo = Datarepository()

    def add_entry_from_df(self, df):
        self.__data_repo.add_entry_from_df(df)

    def get_info(self, location_name='Basel'):
        df = self.__data_repo.get_data_by_location_name(location_name)
        print(df.head(2))
        df.info()

    def get_rainfall(self, location_name='Basel'):
        df = self.__data_repo.get_all_rainfall(location_name)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        grouped_weekly = df.groupby(pd.Grouper(key='timestamp', freq='D')).agg({'precipation': 'sum'}).reset_index()
        grouped_monthly = grouped_weekly.groupby(pd.Grouper(key='timestamp', freq='M')).agg({'precipation': 'mean'}).reset_index()

        plt.bar(grouped_weekly['timestamp'], height=grouped_weekly['precipation'])
        plt.plot(grouped_monthly['timestamp'], grouped_monthly['precipation'], linestyle='dotted', marker='o', color='b', label='Gestippelde lijn')
        plt.xlabel('Datum')
        plt.ylabel('Neerslag in mm')
        plt.title(f'Neerslag in {location_name}')
        plt.legend(['Gemeiddelde neerslag per maand', 'Weekelijkse neerslag'], loc="upper left")
        plt.show()

    def to_csv(self, timeperiod=None, location_name='Basel'):
        df = self.__data_repo.get_data_by_location_name(location_name)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        if timeperiod.upper() in ['D', 'W', 'M']:
            df = df.groupby(pd.Grouper(key='timestamp', freq=timeperiod)).agg({'precipation': 'sum', 'sunshine': 'sum', 'temperature': 'mean', 'pressure': 'mean', 'wind_gust': 'mean'}).reset_index()
        name = location_name+'_export.csv'
        if not os.path.exists('export'):
            map_location = self.create_map('export')
        else:
            map_location = os.path.join(os.getcwd(), 'export')
        location = os.path.join(map_location, name)
        if os.path.exists(location):
            self.check_file(location)

        df.to_csv(location, encoding='utf-8')
        print('csv has been saved on location: ', location)

    def create_map(self, map_name):
        cwd = os.getcwd()
        os.mkdir(map_name)
        cwd = os.path.join(cwd, map_name)
        return cwd

    def check_file(self, location):
        invalid_input = True
        while invalid_input:
            delete = input('Dit bestand bestaat al, wilt u deze verwijderen Ja/Nee').upper()
            if delete.upper() in ['Y', 'YES', 'J', 'JA']:
                os.remove(location)
                invalid_input = False
            elif delete in ['N', 'NO', 'NEE']:
                print('The file could not be saved, request an other city or remove the file on location', location)
                exit(-1)
            else:
                print(f'{delete} is an invalid input.')

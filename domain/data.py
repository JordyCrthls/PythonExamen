# domain.setupdomain.py

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from db.datarespository import Datarepository


class DataDomain:
    def __init__(self):
        self.__data_repo = Datarepository()

    def add_entry_from_df(self, df):
        self.__data_repo.add_entry_from_df(df)

    def get_info(self, location_name):
        df = self.__data_repo.get_data_by_location_name(location_name)
        print(df.head(2))
        df.info()

    def get_rainfall(self):
        df = self.__data_repo.get_all_rainfall()
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        grouped_weekly = df.groupby(pd.Grouper(key='timestamp', freq='D')).agg({'precipation': 'sum'}).reset_index()
        grouped_monthly = grouped_weekly.groupby(pd.Grouper(key='timestamp', freq='M')).agg({'precipation': 'mean'}).reset_index()

        # Plotting the bar chart
        plt.bar(grouped_weekly['timestamp'], height=grouped_weekly['precipation'])
        plt.plot(grouped_monthly['timestamp'], grouped_monthly['precipation'], linestyle='dotted', marker='o', color='b', label='Gestippelde lijn')
        plt.xlabel('Date')
        plt.ylabel('Precipitation')
        plt.title('Daily Precipitation')
        plt.show()

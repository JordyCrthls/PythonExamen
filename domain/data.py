from db.datarespository import Datarepository


class DataDomain:
    def __init__(self, database_name):
        self.__data_repo = Datarepository(database_name)

    def add_entry_from_df(self, df):
        self.__data_repo.add_entry_from_df(df)

    def get_info(self, location_name):
        df = self.__data_repo.get_data_by_location_name(location_name)
        print(df.head(2))
        df.info()

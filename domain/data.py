
from db.datarespository import Datarepository
class DataDomain:
    def __init__(self, database_name):
        self.__data_repo = Datarepository(database_name)

    def add_entry(self, entry):
        self.__data_repo.add_entry(entry)

    def add_entry_from_df(self, df):
        self.__data_repo.add_entry_from_df(df)
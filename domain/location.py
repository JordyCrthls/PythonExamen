# domain.location.py

from db.locationrepository import Locationrepository


class LocationDomain:
    def __init__(self):
        self.__location_repo = Locationrepository()

    def get_location(self, location_name):
        return self.__location_repo.get_location_by_name(location_name)

    def get_location_by_name(self, name):
        return self.__location_repo.get_location_by_name(name)

    def add_location(self, location):
        return self.__location_repo.add_location(location)
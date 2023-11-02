# Main.Repository.locationrepository.py

class Locationrepository:

    def __init__(self, connection):
        self.__connection = connection

    def get_new_id(self):
        query = "count(*) from locations"

    def location_exists(self, location_name):
        query = "select 1 from location where id like ?"

        try:
            cursor = self.__connection.get_connection().cursor()
            cursor.execute(query, (location_name.strip(),))
            result = cursor.fetchall()
        except Exception as e:
            print('error', e)

        return len(result) >= 1

    def add_location(self):
        print('location added')

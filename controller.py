# controller.py

import sys
from domain.setupdomain import SetupDomain
from domain.data import DataDomain

script_name, command = sys.argv

if len(sys.argv) != 2:
    print("Geef minimaal 2 argument op.")

csv = "src.csv"
setup = SetupDomain(csv)
data_domain = DataDomain()


def is_empty_or_none(value):
    return value.upper() in ['', 'NONE']


match command:
    case 'init':
        csv = input("Geef een csv bestand op, of druk op enter voor het standaard bestand.")
        setup.set_src(csv)
        setup.instantiate()

    case 'set_src':
        csv = input("Geef een csv bestand op, of druk op enter voor het standaard bestand.")
        setup.set_src(csv)

    case 'data-info':
        location_name = input('geef de naam van de gewenste locatie op, of druk op enter voor Basel.')

        if is_empty_or_none(location_name):
            location_name = 'Basel'

        data_domain.get_info(location_name)

    case 'rainfall':
        location_name = input('geef de naam van de gewenste locatie op, of druk op enter voor Basel.')

        if is_empty_or_none(location_name):
            location_name = 'Basel'

        data_domain.get_rainfall()

    case 'to_csv':
        location_name = input('geef de naam van de gewenste locatie op, of druk op enter voor Basel.')
        invalid_input = True

        while invalid_input:
            time_period = input(
                'Data kan samengevoegd worden per dag (D), week(W), maand(M) of niet dit is de standaard optie.')
            invalid_input = time_period.upper() not in ['D', 'W', 'M', 'NONE', '']

        if is_empty_or_none(invalid_input):
            invalid_input = None

        if location_name == '':
            location_name = 'Basel'

        data_domain.to_csv(time_period, location_name)

exit(0)

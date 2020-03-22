from pandas import DataFrame


class DataProvider:
    def get_data(self):
        pass


class DataWithPossibilitiesData:
    def get_data(self):
        pass


class TiresDataProvider(DataProvider):
    def get_data(self):
        array = [
            [90, 85, 82, 95],
            [82, 91, 92, 90],
            [80, 90, 80, 87],
            [94, 91, 75, 78]
        ]
        return DataFrame(array,
                         index=['Typ 1', 'Typ 2', 'Typ 3', 'Typ 4'],
                         columns=['Warunek 1', 'Warunek 2', 'Warunek 3', 'Warunek 4'])


class FootballDataProvider(DataProvider):
    def get_data(self):
        array = [
            [8, 5, 6, 7, 8],
            [9, 7, 11, 5, 6],
            [7, 7, 7, 7, 7]
        ]

        return DataFrame(array,
                         index=['Typ 1', 'Typ 2', 'Typ 3'],
                         columns=['Warunek 1', 'Warunek 2', 'Warunek 3', 'Warunek 4', 'Warunek 5'])


class FarmerDataProvider(DataProvider):
    def get_data(self):
        array = [
            [30, 25, 20],
            [28, 20, 22],
            [13, 15, 20],
            [22, 22, 22]
        ]

        return DataFrame(array,
                         index=['Typ A', 'Typ B', 'Typ C', 'Typ D'],
                         columns=['Stan natury 1', 'Stan natury 2', 'Stan natury 3'])


class FuelDataProvider(DataWithPossibilitiesData):
    def get_data(self):
        array = [
            [400, 300, 50],
            [500, 400, 0],
            [700, 500, -200]
        ]

        frame = DataFrame(array,
                          index=['Zmniejszenie zatrudnienia', 'Zatrudnienie bez zmian', 'Zwiększenie zatrudnienia'],
                          columns=['Spada', 'Nie zmienia się', 'Rośnie'])
        possibilities = {"Spada": 0.2, "Nie zmienia się": 0.2, "Rośnie": 0.6}
        return frame, possibilities

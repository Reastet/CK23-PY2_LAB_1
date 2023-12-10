from typing import Union

class Washing_machine:
    def __init__(self, current_model: str, release_year: int, capacity: Union[int, float]):
        '''
        Инициализация объекта "стиральная машина"
        :param current_model: модель машинки у ее владельца
        :param release_year: год выпуска машинки
        :param capacity: вместимость машинки
        Пример:
        >>> my_machine = Washing_machine("Bosh", 2020, 5.3)
        '''
        if not isinstance(current_model, str):
            TypeError("Incorrect type of current_model")
        self.model = current_model
        if not isinstance(release_year, int):
            TypeError("Incorrect type of release_year")
        self.release_year = release_year
        if not isinstance(capacity, (int, float)):
            raise TypeError("Incorrect type of Capacity")
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.capacity = float(capacity)

    def change_model(self, new_model :str)->None:
        '''Устанавливает новое значение модели
        :param new_model: новое значение модели
        Пример:
        >>> myMachine = Washing_machine("Bosh", 2020, 5.3)
        >>>myMachine.change_model("Dexp")'''
        ...
    def change_year(self, new_year : int)->None:
        '''Устанавливает новое значение года выпуска
        :param new_year: новое значение года выпуска
        Пример:
        >>> myMachine = Washing_machine("Bosh", 2020, 5.3)
        >>>myMachine.change_year(2021)'''
        ...

    def change_capacity(self, new_capacity : Union[float, int])->None:
        '''Устанавливает новое значение вместимости
        :param new_capacity: новое значение вместимости
        Пример:
        >>> myMachine = Washing_machine("Bosh", 2020, 5.3)
        >>>myMachine.change_capacity(4.8)'''
        ...
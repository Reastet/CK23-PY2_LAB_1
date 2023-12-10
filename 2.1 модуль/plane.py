from typing import Union


class Plane:

    def __init__(self, cur_speed: Union[float, int], cur_fuel_value: Union[float, int], cur_num_of_pas: int):
        '''
        Создание и подготовка объекта "Самолет"
        :param cur_speed: скорость самолета
        :param cur_fuel_value: объем топлива
        :param cur_num_of_pas: количество пассажиров
        пример:
        >>>cur_plane = Plane(500, 100, 25)

        '''
        if not isinstance(cur_speed, (int, float)):
            raise TypeError("Скорость должна быть типа float или int")
        if cur_speed < 0:
            raise ValueError("Скорость должна быть неотрицательным числом")
        self.speed = float(cur_speed)

        if not isinstance(cur_fuel_value, (int, float)):
            raise TypeError("Объем бака должен быть типа float или int")
        if cur_fuel_value < 0:
            raise ValueError("Объем должен быть неотрицательным числом")
        self.fuel_value = float(cur_fuel_value)

        if not isinstance(cur_num_of_pas, int):
            raise TypeError("Количество пассажиров должно быть типа int")
        if cur_num_of_pas < 0:
            raise ValueError("Объем должен быть неотрицательным числом")
        self.passangers = cur_num_of_pas

    def add_fuel(self, addictive_fuel: Union[float, int]) -> None:
        '''
            Добавляет топливо в бак
            :param addictive_fuel: объем добавляемого топлива (значение может быть отрицательным, тогда топливо уменьшается
            Пример
            >>>cur_plane = Plane(500, 100, 25)
            >>>cur_plane.add_fuel(30)

            '''
        ...

    def change_velocity(self,new_Velocity: Union[float, int]) -> None:
        '''
            Ставит новую скорость
            :param new_Velocity: новая скорость, только положительная
            Пример
            >>>cur_plane = Plane(500, 100, 25)
            >>>cur_plane.change_velocity(30)

            '''
        ...
    def change_num_of_pass(self,new_num_of_pass: int) -> None:
        '''
            Устанавливает новое количество пассажиров
            :param new_num_of_pass: новое количество пассажиров, только положительное
            Пример
            >>>cur_plane = Plane(500, 100, 25)
            >>>cur_plane.change_num_of_pass(30)

            '''
        ...


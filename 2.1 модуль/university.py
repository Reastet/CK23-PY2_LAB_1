class University:
    def __init__(self, num_of_free_learn : int, num_of_tate_learn: int, num_of_teachers: int):
        '''
        Инициализация объекта "Институт"
        :param num_of_free_learn: количество бюджетных мест
        :param num_of_tate_learn: количество контрактных мест
        :param num_of_teachers: количество преподавателей
        Пример:
        >>>polytech = University(100000, 10000000000000, 1000)

        '''
        if not isinstance(num_of_free_learn, int):
            TypeError("Incorrect type of num_of_free_learn")
        if num_of_free_learn<0:
            ValueError("num_of_free_learn can`t be less than 0")
        self.free_learn = num_of_free_learn

        if not isinstance(num_of_tate_learn, int):
            TypeError("Incorrect type of num_of_tate_learn")
        if num_of_tate_learn<0:
            ValueError("num_of_tate_learn can`t be less than 0")
        self.tate_learn = num_of_tate_learn

        if not isinstance(num_of_teachers, int):
            TypeError("Incorrect type of num_of_teachers")
        if num_of_teachers<0:
            ValueError("num_of_teachers can`t be less than 0")
        self.teachers = num_of_teachers

    def update_free_learns(self, new_num_of_free_learn : int)->None:
        '''
        Меняет значение бюджетных мест
        :param new_num_of_free_learn: новое число бюджетных мест
        Пример:
        >>>polytech = University(100000, 10000000000000, 1000)
        >>>polytech.update_free_learns(30)
        '''
        ...

    def update_tate_learns(self, new_num_of_tate_learn : int)->None:
        '''
        Меняет значение бюджетных мест
        :param new_num_of_tate_learn: новое число контрактных мест
        Пример:
        >>>polytech = University(100000, 10000000000000, 1000)
        >>>polytech.update_tate_learns(30)
        '''
        ...

    def update_teachers(self, new_num_of_teachers : int)->None:
        '''
        Меняет значение числа учителей
        :param new_num_of_teachers: новое число бюджетных мест
        Пример:
        >>>polytech = University(100000, 10000000000000, 1000)
        >>>polytech.update_teachers(30)
        '''
        ...
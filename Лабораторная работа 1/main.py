# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union


class Reducer:
    def __init__(self, stages: int, lubricant: str, lubricant_level: Union[int, float]):
        """
                Создание и подготовка к работе объекта "Редуктор"

                :param stages: Количество ступеней редуктора
                :param lubricant: Название масла, спользуемое в редукторе
                :param lubricant_level: Уровень масла в редукторе в мм

                Примеры:
                >>> gear_box = Reducer(3, "И-50", 50)  # инициализация экземпляра класса
                """
        if not isinstance(stages, int):
            raise TypeError("Количество ступеней должно быть типа int")
        if stages <= 0:
            raise ValueError("Количество ступеней должно быть положительным числом")
        self.stages = stages

        if not isinstance(lubricant, str):
            raise TypeError("Название масла должно быть типа str")
        self.lubricant = lubricant

        if not isinstance(lubricant_level, (int, float)):
            raise TypeError("Уровень масла должен быть типа int или float")
        if lubricant_level < 0:
            raise ValueError("Уровень масла не должен быть отрицательным числом")
        self.lubricant_level = lubricant_level

    def add_lubricant(self, lubricant_amount: Union[int, float]) -> None:
        """
        Добавление масла в редуктор.
        :param lubricant_amount: Количество добавленного масла в мм

        Примеры:
        >>> gear_box = Reducer(3, "И-50", 50)
        >>> gear_box.add_lubricant(40)
        """
        if not isinstance(lubricant_amount, (int, float)):
            raise TypeError("Количество добавленного масла должно быть типа int или float")
        if lubricant_amount < 0:
            raise ValueError("Количество добавленного масла должно быть положительным числом")
        ...

    def change_lubricant(self, lubricant: str, lubricant_amount: Union[int, float]) -> None:
        """
        Замена масла в редукторе.
        :param lubricant: Название масла
        :param lubricant_amount: Количество масла в мм

        Примеры:
        >>> gear_box = Reducer(3, "И-50", 50)
        >>> gear_box.change_lubricant("И-30", 40)
        """

        if not isinstance(lubricant, str):
            raise TypeError("Название масла должно быть типа str")
        if not isinstance(lubricant_amount, (int, float)):
            raise TypeError("Количество добавленного масла должно быть типа int или float")
        if lubricant_amount < 0:
            raise ValueError("Количество добавленного масла не должно быть отрицательным числом")
        ...


class Frigde:
    def __init__(self, eggs: int, milk: Union[int, float]):
        """
                Создание и подготовка к работе объекта "Холодильник"

                :param eggs: Количество яиц в холодильнике
                :param milk: Объем молока в холодильнике в литрах

                Примеры:
                >>> frigde1 = Frigde(8, 1.12)  # инициализация экземпляра класса
                """
        if not isinstance(eggs, int):
            raise TypeError("Количество яиц должно быть типа int")
        if eggs < 0:
            raise ValueError("Количество яиц не должно быть отрицательным числом")
        self.eggs = eggs

        if not isinstance(milk, (int, float)):
            raise TypeError("Количество молока должно быть типа int или float")
        if milk < 0:
            raise ValueError("Количество молока не должно быть отрицательным числом")
        self.milk = milk

    def add_eggs(self, eggs: int) -> None:
        """
        Добавление яиц в холодильник.
        :param eggs: Количество добавленных яиц

        Примеры:
        >>> frigde1 = Frigde(8, 1.12)
        >>> frigde1.add_eggs(20)
        """
        if not isinstance(eggs, int):
            raise TypeError("Количество добавленных яиц должно быть типа int")
        if eggs <= 0:
            raise ValueError("Количество добавленных яиц должно быть положительным числом")
        ...

    def remove_eggs(self, eggs_to_take: int) -> None:
        """
        Взятие яиц из холодильника.
        :param eggs_to_take: Количество взятых яиц

        Примеры:
        >>> frigde1 = Frigde(8, 1.12)
        >>> frigde1.remove_eggs(6)
        """

        if not isinstance(eggs_to_take, int):
            raise TypeError("Количество взятых яиц должно быть типа int")
        if eggs_to_take <= 0:
            raise ValueError("Количество взятых яиц должно быть положительным числом")
        if eggs_to_take > self.eggs:
            raise ValueError("Количество взятых яиц не должно превышать количество яиц в холодильнике")
        ...

    def add_milk(self, milk: Union[int, float]) -> None:
        """
        Добавление яиц в холодильник.
        :param milk: Количество добавленных яиц

        Примеры:
        >>> frigde1 = Frigde(8, 1.12)
        >>> frigde1.add_milk(20)
        """
        if not isinstance(milk, (int, float)):
            raise TypeError("Количество добавленного молока должно быть типа int или float")
        if milk <= 0:
            raise ValueError("Количество добавленного молока должно быть положительным числом")
        ...


class Car:
    def __init__(self, mass: int, fuel: Union[int, float], speed: int):
        """
                Создание и подготовка к работе объекта "Автомобиль"

                :param mass: Масса автомобиля в кг
                :param fuel: Объем топлива в литрах
                :param speed: Скорость движения в км/ч

                Примеры:
                >>> car1 = Car(2500, 150, 60)  # инициализация экземпляра класса
                """
        if not isinstance(mass, int):
            raise TypeError("Масса автомобиля должна быть типа int")
        if mass <= 0:
            raise ValueError("Масса автомобиля должна быть положительным числом")
        self.mass = mass

        if not isinstance(fuel, (int, float)):
            raise TypeError("Объем топлива должен быть типа int или float")
        if fuel < 0:
            raise ValueError("Объем топлива не должен быть отрицательным числом")
        self.fuel = fuel

        if not isinstance(speed, int):
            raise TypeError("Скорость автомобиля должна быть типа int")
        if speed < 0:
            raise ValueError("Скорость автомобиля не должна быть отрицательным числом")
        self.speed = speed

    def add_fuel(self, fuel_amount: Union[int, float]) -> None:
        """
        Заправка автомобиля топливом.
        :param fuel_amount: Количество добавленного топлива в литрах

        Примеры:
        >>> car1 = Car(2500, 40, 0)
        >>> car1.add_fuel(100)
        """
        if not isinstance(fuel_amount, (int, float)):
            raise TypeError("Количество добавленного топлива должно быть типа int или float")
        if fuel_amount <= 0:
            raise ValueError("Количество добавленного топлива должно быть положительным числом")
        ...

    def drive(self, speed: int, time: int) -> Union[int, float]:
        """
        Вычисление оставшегося топлива после езды определенное количество времени.
        :param speed: Скорость езды в км/ч
        :param time: Время езды в минутах

        :return: Оставшееся количество топлива

        Примеры:
        >>> car1 = Car(2500, 120, 0)
        >>> car1.drive(60, 180)
        """

        if not isinstance(speed, int):
            raise TypeError("Скорость автомобиля должна быть типа int")
        if speed < 0:
            raise ValueError("Скорость автомобиля не должна быть отрицательным числом")
        if not isinstance(time, int):
            raise TypeError("Время движения автомобиля должна быть типа int")
        if time <= 0:
            raise ValueError("Время движения автомобиля должна быть положительным числом")


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()

class Beverage:
    """
    Класс описывает модель напитка.
    """
    def __init__(self, volume: float, sugar: float):
        """
        Инициализация экземпляра класса напиток.

        :param volume: объем напитка в литрах. Может быть увеличен или уменьшен.
        :param sugar: содержание сахара в процентах. Не может быть уменьшен.
        """
        self.volume = volume
        self._sugar = sugar

    def __str__(self) -> str:
        return f"Объем напитка {self.volume}. Содержание сахара {self.sugar}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(volume={self.volume}, sugar={self.sugar})"

    @property
    def volume(self) -> float:
        return self._volume

    @volume.setter
    def volume(self, volume: float) -> None:
        if volume is not float:  # проверяем что объем типа float
            raise TypeError("volume must be float")
        elif volume < 0:  # проверяем что объем положительный
            raise ValueError("volume must be grater than 0")
        else:
            self._volume = volume

    @property
    def sugar(self) -> float:
        return self._sugar

    def add_sugar(self, sugar: float) -> None:
        """
        Метод увеличивает содержание сахара.

        :param sugar: увеличение содержания сахара в процентах.
        """
        ...

    def cooldown(self, volume: float) -> None:
        """
        Метод для охлаждения напитка, путем добавления воды.

        :param volume: объем добавленной воды в литрах.
        """
        ...


class Coffee(Beverage):
    """
    Класс описывает модель кофе.
    """
    def __init__(self, volume: float, sugar: float, milk: float):
        """
        Инициализация экземпляра класса кофе.
        Дочерний класс класса напиток.

        :param milk: содержание молока в процетнах. Не может быть уменьшен.
        """
        super().__init__(volume=volume, sugar=sugar)
        self._milk = milk

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(volume={self.volume}, sugar={self.sugar}, milk={self.milk})"

    @property
    def milk(self) -> float:
        return self._milk

    def add_milk(self, milk: float) -> None:
        """
        Метод увеличивает содержание молока.

        :param milk: увеличение содержания молока в процентах.
        """
        ...

    def cooldown(self, volume: float) -> None:
        """
        Метод для охлаждения напитка, путем добавления молока.

        :param volume: объем добавленного молока в литрах.

        Метод перегружен, так как увеличивает содержание молока в кофе.
        """
        ...


if __name__ == "__main__":
    # Write your solution here
    pass

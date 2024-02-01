class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name=name, author=author)
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages):
        if pages is not int:
            raise TypeError("pages must be an integer")
        elif pages < 1:
            raise ValueError("pages must be grater than 1")
        else:
            self._pages = pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name=name, author=author)
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

    @property
    def duration(self):
        return self.duration

    @duration.setter
    def duration(self, duration):
        if duration is not float:
            raise TypeError("duration must be float")
        elif duration < 0:
            raise ValueError("duration must be grater than 0")
        else:
            self._duration = duration

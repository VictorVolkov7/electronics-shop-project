from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Создание экземпляра класса Phone.

        Атрибуты родительского класса Item:
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.

        Атрибуты дочернего класса Phone:
        :param number_of_sim: Количество симкарт.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __str__(self):
        """
        Возвращает информацию для пользователей.
        """
        return self.name

    def __repr__(self):
        """
        Возвращает информацию для отладки.
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        """
        Возвращает количество симкарт
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim):
        """
        Проверяет количество симкарт в телефоне (количество должно быть целым числом больше нуля).
        """
        if new_number_of_sim <= 0 and isinstance(new_number_of_sim, int):
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.__number_of_sim = new_number_of_sim

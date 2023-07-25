import csv

from settings import CSV_PATH
from src.instantiate_csv_error import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    csv_path = CSV_PATH
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        super().__init__()

        Item.all.append(self)

    def __repr__(self):
        """
        Возвращает информацию для отладки.
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Возвращает информацию для пользователей.
        """
        return self.__name

    def __add__(self, other):
        """
        Складывает товары по их количеству в магазине.
        """
        if not isinstance(other, self.__class__):
            raise Exception('Это товар не на учете магазина.')
        return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self) -> str:
        """
        Возвращает наименование товара
        """
        return self.__name

    @name.setter
    def name(self, product_name):
        """
        Проверяет, что длина наименования товара не больше 10 символов.
        Обрезает строку (если больше 10 символов)
        """
        if len(product_name) <= 10:
            self.__name = product_name
        else:
            cut_name = product_name[:10]
            self.__name = cut_name

    @classmethod
    def instantiate_from_csv(cls):
        """
        Инициализирует экземпляры класса Item данными из файла src/items.csv
        """
        cls.all = []

        if not cls.csv_path.exists():
            raise FileNotFoundError('Отсутствует файл items.csv')

        with open(cls.csv_path, encoding='Windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)

            for dict_product in reader:
                if len(dict_product) != 3:
                    raise InstantiateCSVError('Файл items.csv поврежден')
                dict_product: dict
                cls(**dict_product)

    @staticmethod
    def string_to_number(number_string: str) -> int:
        """
        Возвращает число из числа-строки.
        """
        if '.' in number_string:
            return int(float(number_string))
        return int(number_string)

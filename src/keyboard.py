from src.item import Item


class MixinKb:

    def __init__(self, lang='EN'):
        self.lang = lang

    @property
    def language(self):
        return self.lang

    def change_lang(self):
        self.lang = "RU" if self.language == "EN" else "EN"
        return self


class Keyboard(Item, MixinKb):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

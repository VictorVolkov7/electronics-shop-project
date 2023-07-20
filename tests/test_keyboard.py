from src.keyboard import MixinKb


def test_keyboard_init(data_for_keyboard):
    assert data_for_keyboard.name == 'Dark Project KD87A'
    assert data_for_keyboard.price == 9600
    assert data_for_keyboard.quantity == 5


def test_mixinkb_init(data_for_keyboard):
    assert data_for_keyboard.lang == 'EN'


def test_mixinkb_language(data_for_keyboard):
    assert data_for_keyboard.language == 'EN'


def test_mixinkb_change_lang(data_for_keyboard):
    data_for_keyboard.change_lang()
    assert data_for_keyboard.language == 'RU'

    data_for_keyboard.change_lang()
    assert data_for_keyboard.language == 'EN'

    data_for_keyboard.change_lang().change_lang()
    assert data_for_keyboard.language == 'EN'



def test_init(data_for_instantiate_error):
    assert data_for_instantiate_error.message == 'Файл items.csv поврежден'


def test_str(data_for_instantiate_error):
    assert str(data_for_instantiate_error) == 'InstantiateCSVError: Файл items.csv поврежден'

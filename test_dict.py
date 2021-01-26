import pytest

dict_sample = {"Company":"Toyota", "model":"Camry", "year": 2021}
def test_dict_sample():
    dict_sample["Capacity"] = "1200CC"
    assert  len(dict_sample) == 4

data_dict_sample = {"City":"Moscow", "Country": "Russia"}
def test_dict_sample_del():
    del data_dict_sample["City"]
    assert data_dict_sample == {"Country": "Russia"}

data_dict_pop = {"Russia": "Country", "Predator": "Lyon", "Alien":"Arnold"}
def test_dict_pop():
    data_dict_pop.popitem()
    assert len(data_dict_pop) == 2

data_dict_clear = {"People": "Russian", "Ukraina":"Kiev"}
def test_dict_clear():
    data_dict_clear.clear()
    assert data_dict_clear == {}

from main import geo_log, unique_val, chanal
from data import for_test_func_chanal
from decimal import Decimal
import pytest


@pytest.mark.parametrize("some_country, some_city",
    [("Россия", "Москва"), ("Индия", "Дели"), ("Португалия", "Лиссабон")]
)
def test_geo_log(some_country, some_city):
    res = geo_log(some_country)
    assert isinstance(res, list)
    test_list = []
    for item in res:
        test_list.append(*item.values())
    join_test_list = sum(test_list, [])
    assert some_city in join_test_list


@pytest.mark.parametrize("number", [213, 15, 54, 119, 98, 35])
def test_unique_val(number):
    res = unique_val()
    assert isinstance(res, list)
    assert unique_val().count(number) == 1
    for item in res:
        assert isinstance(item, int)


@pytest.mark.parametrize("some_dict, expected", for_test_func_chanal)
def test_chanal(some_dict, expected):
    res = chanal(some_dict)
    assert res == expected
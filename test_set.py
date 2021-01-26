import pytest

test_words_set = ["hello", "hello"]
def test_set():
    assert set(test_words_set) == {"hello"}

test_isdis = {2,3,4}
y_isdis = {69,7,6}
def test_isdisjoint():
    result_one = test_isdis.isdisjoint(y_isdis)
    assert result_one == True

test_x_inter = {2, 3, 4, 5,6}
test_y_int = {2, 4}
def test_set_intersection():
    result_two = test_x_inter.intersection(test_y_int)
    assert result_two == {2, 4}

test_data_summ = {1,2,3,4,5}
test_data_summetric = {1,2,3}
def test_summetric_difference():
    test_zeplin = test_data_summ.symmetric_difference(test_data_summetric)
    assert test_zeplin == {4,5}






import  pytest

test_str_isLower = "ghjol,hnfdecdchjj"
def test_islower():
    assert test_str_isLower.islower() == True

test_title_is = "Predator"
def test_istitle():
    assert test_title_is.istitle() == True

test_str_strip = " Tyyy "
def test_strip():
    result_str = test_str_strip.strip()
    assert len(result_str) == 4

test_str_int = "f,h,f"
def test_int_isdigit():
    assert len(test_str_int) == 5



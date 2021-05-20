import pytest
from leapYear import leapYear

l1 = leapYear()

def test_true():
    assert l1.leapYear(2016) == True
    assert l1.leapYear(2020) == True
    assert l1.leapYear(2012) == True

def test_false():
    assert l1.leapYear(2017) == False
    assert l1.leapYear(1927) == False
    assert l1.leapYear(1986) == False

def test_typeerror():
    with pytest.raises(TypeError) as e_info:
        l1.leapYear('a')
        l1.leapYear('hello')
        l1.leapYear(1.0)
        
import pytest
import get_place

def test_place(city):
    z = get_place.place(city)
    b = str()
    for i in z['Places']:
        if city == i['PlaceName']:
            b = i['PlaceName']
    assert b == city
test_place("Kraków")

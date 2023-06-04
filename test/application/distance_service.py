import pytest
from unittest.mock import patch
from haversine import Unit

from src.application.distance_service import haversine_two_cities_km, city_to_coordinates, haversine_distance


def test_haversine_distance():
    coord1 = (51.5072, -0.1276)  # London
    coord2 = (48.8566, 2.3522)  # Paris

    result = haversine_distance(coord1, coord2, unit=Unit.KILOMETERS)

    assert abs(result - 343) < 1, f"Expected the result to be close to 343, but got {result}"

def test_city_to_coordinates():
    city_dict = {'latitude': 51.5072, 'longitude': -0.1276}
    result = city_to_coordinates(city_dict)
    assert result == (51.5072, -0.1276)

@patch('src.application.distance_service.get_city_by_name')
def test_haversine_two_cities_km(mock_get_city_by_name):
    # Mock city data
    oslo_data = {'latitude': 59.9139, 'longitude': 10.7522}
    milan_data = {'latitude': 45.4668, 'longitude': 9.1905}

    mock_get_city_by_name.side_effect = [oslo_data, milan_data]

    city_name_1 = "Oslo"
    city_name_2 = "Milan"
    result = haversine_two_cities_km(city_name_1, city_name_2)

    # Check that the result is close to the expected value
    assert abs(result - 1610) < 0.5, f"Expected the result to be close to 1610km, but got {result}"

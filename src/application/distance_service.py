from haversine import haversine, Unit
from src.infrastructure.city_api.city_client import get_city_by_name


def haversine_between_two_cities(city_name_1, city_name_2):
    city1 = get_city_by_name(city_name_1)
    if city1 is None:
        raise Exception(f'City {city_name_1} not found')
    city2 = get_city_by_name(city_name_2)
    if city2 is None:
        raise Exception(f'City {city_name_2} not found')

    city1_coordinates = (city1.get('latitude'), city1.get('longitude'))
    city2_coordinates = (city2.get('latitude'), city2.get('longitude'))

    try:
        return haversine(city1_coordinates, city2_coordinates, unit=Unit.METERS)
    except Exception as e:
        print(e)
        raise Exception('Error calculating distance')

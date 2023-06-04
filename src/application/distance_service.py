from haversine import haversine, Unit

from src.application.city_service import get_city_by_name


def haversine_two_cities_km(city_name_1, city_name_2) -> float:
    """
    :param city_name_1:
    :param city_name_2:
    :return: haversine distance between two cities in meters
    """
    city1 = get_city_by_name(city_name_1)
    if city1 is None:
        raise Exception(f'City {city_name_1} not found')
    city2 = get_city_by_name(city_name_2)
    if city2 is None:
        raise Exception(f'City {city_name_2} not found')

    city1_coordinates = (city1.get('latitude'), city1.get('longitude'))
    city2_coordinates = (city2.get('latitude'), city2.get('longitude'))

    try:
        return haversine(city1_coordinates, city2_coordinates, unit=Unit.KILOMETERS)
    except Exception as e:
        print(e)
        raise Exception('Error calculating distance')

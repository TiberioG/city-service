from haversine import haversine, Unit

from src.application.city_service import get_city_by_name


def city_to_coordinates(city_dict) -> tuple[float, float]:
    """
    :param city_dict: todo create model and type
    :return: tuple with latitude and longitude
    """
    return city_dict.get('latitude'), city_dict.get('longitude')


def haversine_distance(coord1: tuple[float, float], coord2: tuple[float, float], unit: Unit) -> float:
    return haversine(coord1, coord2, unit=unit)


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

    city1_coordinates = city_to_coordinates(city1)
    city2_coordinates = city_to_coordinates(city2)

    try:
        return haversine_distance(city1_coordinates, city2_coordinates, unit=Unit.KILOMETERS)
    except Exception as e:
        print(e)
        raise Exception('Error calculating distance')

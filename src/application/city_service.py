from __future__ import annotations

from src.infrastructure.city_api.city_client import call_city_api


def get_city_by_name(name: str) -> dict | None:

    try:
        res = call_city_api(name)
        # this api returns a list of cities, we just want the first one
        # todo check if this is the best way to handle this
        res = res[0] if len(res) > 0 else None

        return res

    except Exception as e:
        return None

def get_cities(query: str) -> list[dict] | None:
    try:
        res = call_city_api(query, limit=20)
        return res

    except Exception as e:
        return None

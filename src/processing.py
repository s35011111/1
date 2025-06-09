from typing import Iterable, Optional


def filter_by_state(data: Optional, state_key: str = "EXECUTED") -> Iterable:
    """принимает список словарей возвращает новый список словарей, содержащий только те словари,
    у которых ключ state_key соответствует указанному значению"""
    result = []
    for item in range(len(data)):
        if data[item]["state"] == state_key:
            result.append(data[item])
    return result


def sort_by_date(data: Optional, sort_order: bool = True) -> Iterable:
    """Функция возвращает новый список, отсортированный по дате"""
    return sorted(data, key=lambda x: x["date"], reverse=sort_order)

from typing import Iterable, Optional


def filter_by_state(dictionary_list: Optional, state_key: str = "EXECUTED") -> Iterable:
    """принимает список словарей возвращает новый список словарей, содержащий только те словари,
    у которых ключ state_key соответствует указанному значению"""
    dictionary_list_result = []
    for item in range(len(dictionary_list)):
        if dictionary_list[item]["state"] == state_key:
            dictionary_list_result.append(dictionary_list[item])
    return dictionary_list_result


def sort_by_date(dictionary_list: Optional, sort_order: bool = True) -> Iterable:
    """Функция возвращает новый список, отсортированный по дате"""
    return sorted(dictionary_list, key=lambda x: x["date"], reverse=sort_order)

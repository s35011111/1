from typing import Any


def filter_by_state(dictionary_list: "Any", state_key: str = "EXECUTED") -> Any:
    """принимает список словарей возвращает новый список словарей, содержащий только те словари,
    у которых ключ state_key соответствует указанному значению"""
    return list(filter(lambda x: x["state"] == state_key, dictionary_list))


def sort_by_date(dictionary_list: "Any", sort_order: bool = True) -> Any:
    """Функция возвращает новый список, отсортированный по дате"""
    return sorted(dictionary_list, key=lambda x: x["date"], reverse=sort_order)


def filter_by_currensy(dictionary_list: "Any") -> Any:
    return list(filter(lambda x: x["currency_code"] == "RUB", dictionary_list))


def filter_by_currensy_json(dictionary_list: "Any") -> Any:
    return list(filter(lambda x: x["operationAmount"]["currency"]["code"] == "RUB", dictionary_list))

import re
from typing import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция принимающая список словарей с данными о банковских операциях и строку поиска, а
    возвращающая список словарей, у которых в описании есть данная строка"""
    result = []
    for i in data:
        if i.get("description"):
            if re.search(search, i.get("description"), flags=re.DOTALL | re.IGNORECASE):
                result.append(i)
    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функцию принимающая список словарей с данными о банковских операциях  и список категорий операций,
    а возвращать словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
    """
    result = []
    for i in data:
        result.append(i["description"])
    temp_list = list(set(result).difference(set(categories)))
    for i in temp_list:
        while result.count(i):
            result.remove(i)
    return Counter(result)


from typing import Iterable, Any, Iterator


def filter_by_currency(dictionary_transactions: Iterable, currency: str) -> Iterator:
    """Функция принимающая на вход список словарей, представляющих транзакциии возвращающая итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    for i in dictionary_transactions:
        if i["operationAmount"]["currency"]["code"] == currency:
            yield i
    while True:
        yield {}


def transaction_descriptions(dictionary_transactions: Iterable) -> Iterator:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for i in dictionary_transactions:
        yield i["description"]
    while True:
        yield ""


def card_number_generator(start: int, end: int) -> Any:
    """Функция выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for i in range(start, end + 1):
        width = 16
        card = str(i).zfill(width)
        block_size = 4
        yield " ".join(card[i : i + block_size] for i in range(0, width, block_size))
    while True:
        yield ""

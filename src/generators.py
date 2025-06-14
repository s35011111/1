from typing import Any


def filter_by_currency(dictionary_transactions: Any, currency: str) -> Any:
    """Функция принимающая на вход список словарей, представляющих транзакциии возвращающая итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    for i in range(len(dictionary_transactions)):
        if dictionary_transactions[i]["operationAmount"]["currency"]["code"] == currency:
            yield dictionary_transactions[i]
    while True:
        yield {}


def transaction_descriptions(dictionary_transactions: Any) -> Any:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for i in range(len(dictionary_transactions)):
        yield dictionary_transactions[i]["description"]
    while True:
        yield ""


def card_number_generator(start: int, end: int) -> Any:
    """Функция выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for i in range(start, end + 1):
        yield form_card_number(i)
    while True:
        yield ""


def form_card_number(card_number: int) -> str:
    """Функция задает формат номера XXXX XXXX XXXX XXXX"""
    card_number_list = list(str(card_number))
    while len(card_number_list) < 16:
        card_number_list.insert(0, "0")
    card_number_list.insert(4, " ")
    card_number_list.insert(9, " ")
    card_number_list.insert(14, " ")
    return "".join(card_number_list)



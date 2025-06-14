from typing import Any

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from tests.conftest import transactions


def test_filter_by_currency(transactions: Any) -> Any:
    generator = filter_by_currency(transactions, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }

    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }

    assert next(generator) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }

    assert next(generator) == {}


def test_transaction_descriptions(transactions: Any) -> Any:
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"
    assert next(generator) == ""


def test_card_number_generator() -> None:
    generator = card_number_generator(1161691861716, 1161691861722)
    assert next(generator) == "0001 1616 9186 1716"
    assert next(generator) == "0001 1616 9186 1717"
    assert next(generator) == "0001 1616 9186 1718"
    assert next(generator) == "0001 1616 9186 1719"
    assert next(generator) == "0001 1616 9186 1720"
    assert next(generator) == "0001 1616 9186 1721"
    assert next(generator) == "0001 1616 9186 1722"
    assert next(generator) == ""

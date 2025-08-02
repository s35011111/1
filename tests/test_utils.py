from typing import Any
from unittest.mock import patch

from src.utils import reading_json, transaction_amount_rub
from tests.conftest import transactions


def test_reading_json() -> Any:

    assert reading_json("C:/Users/Admin/PycharmProjects/PythonProject1/data/operations.json")[1] == {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    assert reading_json("operations.json") == []


def test_transaction_amount_rub(transactions: Any) -> Any:
    assert transaction_amount_rub(transactions[2]) == 43318.34


def test_transaction_amount_rub_0() -> Any:
    assert transaction_amount_rub({}) == 0.0


@patch("requests.get")
def test_transaction_amount_rub_from_usd(mock_requests: Any, transactions: Any) -> Any:
    mock_requests.return_value.text = '{"result":785925.6}'
    assert transaction_amount_rub(transactions[0]) == 785925.6

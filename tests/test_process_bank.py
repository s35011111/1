from typing import Any

from src.process_bank import process_bank_operations, process_bank_search
from tests.conftest import transactions


def test_process_bank_search(transactions: Any) -> Any:
    assert process_bank_search(transactions, "карт.")[0]["date"] == "2018-08-19T04:27:37.904916"
    assert process_bank_search(transactions, "сч.т")[0]["date"] == "2019-04-04T23:20:05.206878"


def test_process_bank_operations(transactions: Any) -> Any:
    assert process_bank_operations(transactions, ["Перевод со счета на счет"]) == {"Перевод со счета на счет": 2}
    assert process_bank_operations(transactions, ["Перевод с карты на карту", "Перевод организации"]) == {
        "Перевод организации": 2,
        "Перевод с карты на карту": 1,
    }

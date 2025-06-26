import csv
from typing import Any
from unittest.mock import mock_open, patch

import pandas as pd

from src.get_data import reading_csv, reading_excel


def test_reading_csv() -> Any:

    assert (
        reading_csv("C:/Users/Admin/PycharmProjects/PythonProject1/data/transactions.csv")[1]["date"]
        == "2020-12-06T23:00:58Z"
    )
    assert reading_csv("transactions.csv") == []


def test_reading_excel() -> Any:
    assert (
        reading_excel("C:/Users/Admin/PycharmProjects/PythonProject1/data/transactions_excel.xlsx")[1]["id"]
        == 3598919.0
    )
    assert reading_excel("transactions_excel.xlsx") == []


def test_reading_csv_() -> Any:
    csv_content = "date\n2019-07-03T18:35:29.512364\n2018-06-30T02:08:58.425572"
    m = mock_open(read_data=csv_content)
    with patch("builtins.open", m):
        result = reading_csv("transactions.csv")
    assert result[0]["date"] == "2019-07-03T18:35:29.512364"
    assert result[1]["date"] == "2018-06-30T02:08:58.425572"

import csv
from typing import Any

import numpy as np
import pandas as pd


def reading_csv(transactions_file: str) -> Any:
    """Функция принимающая на вход путь до csv-файла и возвращает
    список словарей с данными о финансовых транзакциях"""
    try:
        with open(transactions_file, "r", encoding="utf-8") as f:
            result_dict = list(csv.DictReader(f, delimiter=";"))
        return result_dict
    except FileNotFoundError:
        return []


def reading_excel(transactions_file: str) -> Any:
    """Функция принимающая на вход путь до excel-файла и возвращает
    список словарей с данными о финансовых транзакциях"""
    try:
        result_df = pd.read_excel(transactions_file)
        result_df = result_df.replace({np.nan: None}).astype(object)
        result_dict = result_df.to_dict("records")
        return result_dict
    except FileNotFoundError:
        return []

import json
import os
from typing import Any

import requests
from dotenv import load_dotenv


def reading_json(operations_file: str) -> Any:
    """Функция принимающая на вход путь до JSON-файла и возвращает
     список словарей с данными о финансовых транзакциях"""
    try:
        with open(operations_file, "r", encoding="utf-8", errors="replace") as f:  ##""
            result_dict = json.load(f)
        return result_dict
    except (json.JSONDecodeError, TypeError, KeyError, ValueError, FileNotFoundError):
        return []


def transaction_amount_rub(transaction_dict: dict) -> float:
    """Aункцию принимающая на вход транзакцию и возвращает сумму транзакции
     (amount) в рублях"""
    if not transaction_dict:
        return 0.0
    if transaction_dict["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction_dict["operationAmount"]["amount"])

    amount_ = transaction_dict["operationAmount"]["amount"]
    from_ = transaction_dict["operationAmount"]["currency"]["code"]
    to_ = "RUB"

    load_dotenv()
    api_token = os.getenv("API_KEY")
    headers_ = {"apikey": f"{api_token}"}
    response = requests.get(
        f"https://api.apilayer.com/exchangerates_data/convert?to={to_}&from={from_}&amount={amount_}", headers=headers_
    )
    dict_result = json.loads(response.text)
    return round(float(dict_result["result"]), 2)


import json
import logging
import os
from typing import Any

import requests
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("C:/Users/Admin/PycharmProjects/PythonProject1/logs/utils.log", "w")
logger.addHandler(file_handler)
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.setLevel(logging.DEBUG)


def reading_json(operations_file: str) -> Any:
    """Функция принимающая на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях"""
    logger.debug(f": input {operations_file}")
    try:
        with open(operations_file, "r", encoding="utf-8", errors="replace") as f:
            result_dict = json.load(f)
        logger.info(result_dict[0]["date"])
        return result_dict
    except (json.JSONDecodeError, TypeError, KeyError, ValueError, FileNotFoundError) as e:
        logger.error(": %s", e)
        return []


def transaction_amount_rub(transaction_dict: dict) -> float:
    """Функцию принимающая на вход транзакцию и возвращает сумму транзакции
    (amount) в рублях"""
    try:
        logger.debug(f": input {transaction_dict["date"]}")
    except KeyError as e:
        logger.error(": %s", e)
    try:
        if not transaction_dict:
            result = 0.0

        elif transaction_dict["operationAmount"]["currency"]["code"] == "RUB":
            result = float(transaction_dict["operationAmount"]["amount"])
        else:
            amount_ = transaction_dict["operationAmount"]["amount"]
            from_ = transaction_dict["operationAmount"]["currency"]["code"]
            to_ = "RUB"

            load_dotenv()
            api_token = os.getenv("API_KEY")
            headers_ = {"apikey": f"{api_token}"}
            response = requests.get(
                f"https://api.apilayer.com/exchangerates_data/convert?to={to_}&from={from_}&amount={amount_}",
                headers=headers_,
            )
            dict_result = json.loads(response.text)
            result = round(float(dict_result["result"]), 2)
        logger.info(result)
        return result

    except Exception as e:
        logger.error(": %s", e)
        return 0.0

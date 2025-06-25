import logging

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("C:/Users/Admin/PycharmProjects/PythonProject1/logs/mask.log", "w")
logger.addHandler(file_handler)
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:  # XXXX XX** **** XXXX
    """Функция принимает на вход номер карты и возвращает ее маску"""
    logger.debug(f": input {card_number}, {type(card_number)}")
    try:
        if len(card_number) < 6:
            result = f""
        else:
            result = f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    except TypeError as e:
        logger.error(": %s", e)
        return f""

    logger.info(f"result: {result}")
    return result


def get_mask_account(account_number: str) -> str:  # **XXXX
    """Функция принимает на вход номер счета и возвращает его маску"""
    logger.debug(f": input {account_number}, {type(account_number)}")
    try:
        if len(account_number) < 6:
            result = f""
        else:
            result = f"**{account_number[-4:]}"
        logger.info(f"result: {result}")
        return result
    except TypeError as e:
        logger.error(": %s", e)
        return f""

def get_mask_card_number(card_number: str) -> str:  # XXXX XX** **** XXXX
    """Функция принимает на вход номер карты и возвращает ее маску"""
    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:16]}"


def get_mask_account(account_number: str) -> str:  # **XXXX
    """Функция принимает на вход номер счета и возвращает его маску"""
    return f"**{account_number[12:16]}"

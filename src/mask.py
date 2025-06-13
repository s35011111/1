def get_mask_card_number(card_number: str) -> str:  # XXXX XX** **** XXXX
    """Функция принимает на вход номер карты и возвращает ее маску"""
    if len(card_number) < 6:
        return f""
    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:  # **XXXX
    """Функция принимает на вход номер счета и возвращает его маску"""
    if len(account_number) < 6:
        return f""
    return f"**{account_number[-4:]}"

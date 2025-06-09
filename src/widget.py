from src.mask import get_mask_account, get_mask_card_number


def mask_account_card(card_info: str) -> str:  # Visa Platinum 7000 79** **** 6361
    """возвращает строку с замаскированным номером"""
    card_info_list = card_info.split(" ")
    account_name = ""
    account_number = ""
    for i in card_info_list:
        if not i.isdigit() :
            account_name += i
            account_name += " "
        else:
            account_number += i

    if account_name == "Счет ":
        return f"{account_name}{get_mask_account(account_number)}"
    else:
        return f"{account_name}{get_mask_card_number(account_number)}"


#
def get_date(date_info: str) -> str:  # "2024-03-11T02:26:18.671407"
    """принимает на вход строку с датой  и возращает в другом формате"""
    return f"{date_info[8:10]}.{date_info[5:7]}.{date_info[0:4]}"

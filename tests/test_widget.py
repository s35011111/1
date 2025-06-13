from typing import Any

from src.widget import get_date, mask_account_card


def test_mask_account_card() -> Any:
    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"
    assert mask_account_card("Visa Classic 1596837868705199") == "Visa Classic 1596 83** **** 5199"
    assert mask_account_card("Счет 35383033474447895560") == "Счет **5560"
    assert mask_account_card("Visa Gold 30135874") == "Visa Gold 3013 58** **** 5874"
    assert mask_account_card("Счет 779589") == "Счет **9589"
    assert mask_account_card("301") == ""
    assert mask_account_card("MasterCard") == "MasterCard "


def test_get_date() -> Any:
    assert get_date("2019-07-03T18:35:29.512364") == "03.07.2019"
    assert get_date("2018-09-12T21:27:25.241689") == "12.09.2018"
    assert get_date("2018-06-30T02:08:58.425572") == "30.06.2018"
    assert get_date("2018-10-") == ""
    assert get_date("18:35:29.512364") == ""
    assert get_date("20af-ob-30T02:08:58.425572") == ""
    assert get_date("x") == ""

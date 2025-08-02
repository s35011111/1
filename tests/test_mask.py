from typing import Any

import pytest

from src.mask import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number,mask_number",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1596837868705199", "1596 83** **** 5199"),
        ("8990922113665229", "8990 92** **** 5229"),
        ("0007922896063", "0007 92** **** 6063"),
        ("30135874", "3013 58** **** 5874"),
        ("", ""),
        ("35", ""),
        ("870519", "8705 19** **** 0519"),
        ("df5meof", "df5m eo** **** meof"),
    ],
)
def test_get_mask_card_number(number: str, mask_number: str) -> Any:
    assert get_mask_card_number(number) == mask_number


def test_get_mask_account() -> Any:
    assert get_mask_account("64686473678894779589") == "**9589"
    assert get_mask_account(73654108430135874305) == ""
    assert get_mask_account("35383033474447895560") == "**5560"
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("779589") == "**9589"
    assert get_mask_account("301") == ""
    assert get_mask_account("") == ""
    assert get_mask_account("fdsg5nbs") == "**5nbs"

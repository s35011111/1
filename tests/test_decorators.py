from typing import Any, Union

from src.decorators import log


def test_log(capsys: Any) -> None:
    @log()
    def add_numbers(a:Union[int, float] , b:Union[int, float])->Union[int, float]:
        return a + b

    add_numbers(3000, 500)
    captured = capsys.readouterr()
    assert captured.out == "add_numbers ok\n"

    add_numbers("3000", 500)
    captured = capsys.readouterr()
    assert captured.out == "add_numbers error: TypeError. Inputs: ('3000', 500), {}\n"

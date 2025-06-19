from functools import wraps
from typing import Any, Callable


def log(filename: Any = None) -> Callable:
    """декоратор логирующий результаты выполнения функции или возникшие ошибки"""

    def decorator_function(function: Callable) -> Callable:
        @wraps(function)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = function(*args, **kwargs)
                status = "ok"
            except Exception as e:
                status = f"error: {type(e).__name__}"
                result = None
                inputs = f"Inputs: {args}, {kwargs}"
                log_message = f"{function.__name__} {status}. {inputs}"

            else:
                log_message = f"{function.__name__} {status}"

            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(log_message + "\n")
            else:
                print(log_message)
            return result

        return inner

    return decorator_function

import time
from functools import wraps
from typing import Any

from rich import print


def execute_time(limit: float = 1) -> Any:
    """Замер времени."""

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()  # Начало замера
            print(f"\n:timer_clock:  [blue]Замеряем [#FF6F00]{func.__name__}")
            if func.__doc__:
                print(
                    f"\n:page_facing_up: Описание: [#FF6F00]{func.__doc__}\n"
                )
            print(f":stop_sign: [blue]Ограничение [red]{limit}[/red] сек\n")
            result = func(*args, **kwargs)
            end_time = time.time()  # Конец замера
            execution_time = end_time - start_time

            print(
                f"[yellow]:stopwatch:  [italic]Время выполнения: "
                f"[bold][#73FF73]{round(execution_time, 3)}[/#73FF73][/bold] сек :rocket:"
                if execution_time < limit
                else f"[yellow]:stopwatch:  [italic]Время выполнения: "
                f"[bold][red]{round(execution_time, 3)}[/red][/bold] сек :snail:"
            )
            print(
                "\n[green][italic][bold]"
                ":triangular_flag: Результат выполнения: [#FF5937]:arrow_heading_down:\n"
            )
            return result

        return wrapper

    return decorator

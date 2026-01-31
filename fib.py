# fib.py

import functools
import time
from functools import lru_cache
import matplotlib.pyplot as plt
import numpy as np

# storing values to later plot a graph
fib_number = []
time_to_run = []


def timer(func):
    """Printing the runtime of the decorated function"""

    @functools.wraps(func)
    def timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        fib_number.append(args[0])
        time_to_run.append(run_time)
        print(f"Finished in {run_time:.8f}s: f({args[0]}) -> {value}")
        return value

    return timer


@lru_cache
@timer
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    fib(100)
    plt.plot(fib_number, time_to_run)
    plt.grid(axis="y")
    plt.ylabel("Time to Run in Seconds")
    plt.xlabel("Fibonacci Number")
    plt.show()

import asyncio
import time
from time import strftime

from pyflakes.api import main


def decor(func):
    def wrap():
        print("________________________")
        func()
        print("________________________")
    return wrap()

@decor
def print_text():
    print("Hello Word!")

# decorated = decor(print_text)

# print_text()

a, b = 5, 7
a, b = False, True
# if a and b:
#     print(a)
print(a or b)

async def say_after(what, delay):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(say_after('hello', 1))
    task2 = asyncio.create_task(say_after('world', 2))
    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

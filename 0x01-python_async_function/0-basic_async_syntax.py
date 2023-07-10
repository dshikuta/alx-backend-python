#!/usr/bin/env python3
'''The basics of async.
An asynchronous coroutine that takes in an integer
argument (`max_delay`, with a default value of 10) named
`wait_random` that waits for a random delay between 0 and
`max_delay` (included and float value) seconds and returns it.
The `random` module used.

'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''A function to generate a random delay between 0 and max_delay
    '''
    wait_seconds: float = random.random() * max_delay
    await asyncio.sleep(wait_seconds)
    return wait_seconds

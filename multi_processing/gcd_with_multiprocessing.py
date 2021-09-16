"""Calculate GCD without using multiprocessing."""
import time
import random
import logging
import itertools

from multiprocessing import cpu_count
from multiprocessing.pool import Pool


def get_gcd(first_number: int, second_number: int):
    """Get gcd of the two numbers using Euclidean algorithm."""

    if first_number == 0:
        return second_number
    elif second_number == 0:
        return first_number

    remainder = first_number % second_number
    return get_gcd(second_number, remainder)


if __name__ == "__main__":

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    numbers = []
    seeds = [2, 3, 4, 5, 6, 9, 11, 13, 17, 21, 23, 27, 29, 31, 33]

    for seed in seeds:
        for iter in range(100):
            numbers.append((seed * seed) + (seed * iter))

    pairs = list(itertools.combinations(numbers, 2))
    random.shuffle(pairs)

    start_time = time.perf_counter()
    logging.info("Starting execution")

    pool = Pool(processes=cpu_count())
    pool.starmap(get_gcd, pairs)

    end_time = time.perf_counter()
    logging.info(
        f"Finished execution in {end_time - start_time} seconds for {len(pairs)} pairs"
    )

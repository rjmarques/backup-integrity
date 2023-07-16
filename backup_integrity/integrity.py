import os
import math
from tqdm import tqdm
from time import sleep

BLOCK_SIZE = 131072 # 128 KiB

def compare(file_a, file_b, show_progress=True):
    # sanity check, the sizes must be the same
    size_a = os.stat(file_a).st_size
    size_b = os.stat(file_b).st_size
    if size_a != size_b:
        return False

    expected_it = math.ceil(size_a / BLOCK_SIZE)

    with (
        open(file_a, mode='rb', buffering=BLOCK_SIZE) as f1,
        open(file_b, mode='rb', buffering=BLOCK_SIZE) as f2,
    ):
        it1 = iter(lambda: f1.read(BLOCK_SIZE), b'')
        it2 = iter(lambda: f2.read(BLOCK_SIZE), b'')

        disabled = not show_progress
        for blk1, blk2 in tqdm(
                zip(it1, it2),
                disable=disabled,
                leave=False,
                total=expected_it,
                unit="block",
                desc="comparing '{0}' to '{1}'".format(file_a, file_b)
            ):
            if blk1 != blk2:
                return False

    return True
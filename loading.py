from tqdm import tqdm
from time import sleep

def start():
    for i in tqdm (range (101),
                desc="Loading…",
                ascii=False, ncols=75):
        sleep(0.01)
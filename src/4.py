#! /usr/bin/env python

import hashlib
from multiprocessing import Process, Lock, Manager

INPUT = 'iwrupvqb'
STEP = 400000
MAX_PROC = 4
STARTHASH='000000'
iteration_results = Manager().list()


def checkhash(start, end):
    for i in range(start, end):
        s = gethash(INPUT + str(i))
        if s.startswith('000000'):
            iteration_results.append(i)
            break

def gethash(key):
    return hashlib.md5(key).hexdigest()

if __name__ == '__main__':
    rangestart = 0
    l = Lock()
    while True:
        processes = []
        for i in range(0, MAX_PROC):
            p = Process(target=checkhash, args=(rangestart + STEP * i, rangestart + STEP * (i + 1)))
            processes.append(p)
            p.start()
        # Synchronize with the processes
        for p in processes:
            p.join()
        # Check if some process found a result
        if len(iteration_results) > 0:
            print min(iteration_results)
            break
        # Prepare the next iteration
        rangestart = rangestart + MAX_PROC * STEP

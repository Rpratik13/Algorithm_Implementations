import matplotlib.pyplot as plt
from bubbleSort import *
import time
import random

if __name__ == '__main__':
    val = [[], []]
    for i in range(1000, 10001, 1000):
        array = random.sample(range(i), i)
        start = time.time()
        bubbleSort(array)
        end = time.time()
        val[0].append(i)
        val[1].append(end - start)

        print(i)
        print(end - start)

    plt.plot(val[0], val[1])
    plt.show()

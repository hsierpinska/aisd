import numpy as np
import matplotlib.pyplot as plt
from generate import generate_knapsack
import timeit
from Knapsack import Knapsack


def create_plot(arr, title=None, arr2=None):
    """

    Args:


        arr: Lista z czasami operacji
        arr2: Lista z czasami operacji, ale druga
        title: Tytuł wykresu

    Returns:

    """

    fig, ax = plt.subplots()
    ax.plot(np.arange(len(arr)), arr)
    # ax.plot(np.arange(len(arr)), arr, label='Algorytm dynamiczny')
    if arr2:
        ax.plot(np.arange(len(arr2)), arr2, label='aaa')
    # plt.yscale('log')
    # plt.legend(loc="upper left")
    ax.set_xlabel('Pojemność plecaka - c')
    ax.set_ylabel('Czas w sekundach - t')

    if title:
        ax.set_title(title)
    plt.show()


knapsack_times = []

for i in range(1, 1000):
    print(i)
    n = 10
    a = str(i)
    knapsack = generate_knapsack(n, i)

    time1 = timeit.timeit('knapsack.knapsack_brute_force()',
                          setup='\n'
                                'from __main__ import knapsack\n'
                                'a=' + a, number=1)
    knapsack_times.append(time1)
print(knapsack_times)
create_plot(knapsack_times, "Algorytm siłowy, n = 10")

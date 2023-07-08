from Node import Node
from generating_tree import array_to_random_bst, sorted_array_to_avl, generate_data
import numpy as np
import matplotlib.pyplot as plt
import time
import timeit

# Wykonaj 3 wykresy (jeden wykres dla każdej z operacji:
# tworzenie struktury, wyszukanie minimum, wypisanie in-order)
# t=f(n) zależności czasu obliczeń t od liczby n elementów w drzewie.
# Na każdym wykresie przedstaw 2 krzywe – po jednej krzywej dla każdej struktury.
# Wykonaj wykres t=f(n) zależności czasu równoważenia t od liczby n elementów w losowym drzewie BST.

arr_nanoseconds_bst = []  # czas operacji drzewa bst gdzie indeks odpowiada liczbie elementów
arr_nanoseconds_avl = []  # jak wyżej tylko avl



for i in range(1, 100):
    st = time.perf_counter_ns()
    tree = sorted_array_to_avl(np.sort(generate_data(i)))
    et = time.perf_counter_ns()
    arr_nanoseconds_avl.append(et - st)
    st = time.perf_counter_ns()
    tree1 = array_to_random_bst(generate_data(i))
    et = time.perf_counter_ns()
    arr_nanoseconds_bst.append(et - st)


def create_plot(arr, arr2=None, title=None):
    '''

    Args:


        arr: Lista z czasami operacji
        arr2: Opcjonalna lista
        title: Tytuł wykresu

    Returns:

    '''

    fig, ax = plt.subplots()
    ax.plot(np.arange(len(arr)), arr, label='AVL')
    if arr2:
        ax.plot(np.arange(len(arr2)), arr2, label='BST')
    plt.yscale('log')
    # plt.xscale('log')
    plt.legend(loc="upper left")
    ax.set_xlabel('Elementy - n')
    ax.set_ylabel('Czas w nanosekundach - t')
    # ax.text(60, 1 * 10 ** 6, "t=f(n)")
    if title:
        ax.set_title(title)
    plt.show()



for i in range(1,100):
    a = str(i)
    time = timeit.timeit('sorted_array_to_avl(np.sort(generate_data(a)))',
                         setup='import numpy as np\n'
                               'from generating_tree import generate_data, sorted_array_to_avl\n'
                               'a='+a, number=1)
    arr_nanoseconds_avl.append(time * 1e9)
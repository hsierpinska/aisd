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

arr_nanoseconds_avl = []  # czas operacji drzewa avl gdzie indeks odpowiada liczbie elementów
arr_nanoseconds_bst = []  # jak wyżej tylko bst
arr_find_min_avl = []
arr_find_min_bst = []
arr_inorder_avl = []
arr_inorder_bst = []
arr_balance_avl = []
arr_balance_bst = []


def create_plot(arr, arr2=None, title=None):
    """

    Args:


        arr: Lista z czasami operacji na AVL
        arr2: Lista z czasami operacji na BST
        title: Tytuł wykresu

    Returns:

    """

    fig, ax = plt.subplots()
    ax.plot(np.arange(len(arr)), arr, label='AVL')
    if arr2:
        ax.plot(np.arange(len(arr2)), arr2, label='BST')
    plt.yscale('log')
    plt.legend(loc="upper left")
    ax.set_xlabel('Elementy - n')
    ax.set_ylabel('Czas w nanosekundach - t')
    if title:
        ax.set_title(title)
    plt.show()




for i in range(1, 1000):
    avl_tree = sorted_array_to_avl(np.sort(generate_data(i)))
    bst_tree = array_to_random_bst(generate_data(i))
    print(i)
    time5 = timeit.timeit('avl_tree.inorder_print(printing=False)', setup="from __main__ import avl_tree", number=1)
    time6 = timeit.timeit('bst_tree.inorder_print(printing=False)', setup="from __main__ import bst_tree", number=1)
    # time7 = timeit.timeit('avl_tree.balance_dsw()', setup="from __main__ import avl_tree", number=1)
    # time8 = timeit.timeit('bst_tree.balance_dsw()', setup="from __main__ import bst_tree", number=1)
    arr_inorder_avl.append(time5 * 1e9)
    arr_inorder_bst.append(time6 * 1e9)
    # arr_balance_avl.append(time7 * 1e9)
    # arr_balance_bst.append(time8 * 1e9)
arr_inorder_avl = [sum(arr_inorder_avl[i:i + 10]) / 10 for i in
                            range(0, len(arr_inorder_avl))]
arr_inorder_bst = [sum(arr_inorder_bst[i:i + 10]) / 10 for i in
                            range(0, len(arr_inorder_bst))]
# create_plot(arr_nanoseconds_avl, arr_nanoseconds_bst, "Wypisanie in-order")
# create_plot(arr_find_min_avl, arr_find_min_bst, "Znalezienie najmniejszego elementu")
create_plot(arr_inorder_avl, arr_inorder_bst, "Wypisanie in-order")
# create_plot(arr_balance_avl, arr_balance_bst, "Równoważenie drzewa")

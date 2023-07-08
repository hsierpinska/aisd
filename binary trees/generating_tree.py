from Node import Node
import numpy as np
from random import shuffle


def generate_data(num):
    data = set()
    while len(data) != num:
        data.add(np.random.randint(1, 5001))
    shuffled_list = list(data)
    shuffle(shuffled_list)
    return shuffled_list


def input_data(num):
    arr = []
    for _ in range(0, num):
        a = input("Podaj liczbę: ")
        try:
            a = int(a)
            arr.append(a)
        except Exception as e:
            print("Nieprawidłowe dane", e)
    return arr


def sorted_array_to_avl(arr):
    """Funkcja przyjmuje posortowaną rosnąco tablicę arr i zwraca drzewo binarne,
    które ma medianę tej tablicy jako korzeń.

    Args:
        arr (List[int]): Posortowana lista kluczy

    Returns:
        Node | None: Korzeń drzewa (lub None w przypadku tablicy pustej)
    """

    if len(arr) == 0:  # base case
        return None

    # znajdź indeks mediany
    mid = len(arr) // 2

    # mediana jest korzeniem
    root = Node(arr[mid])

    # rekurencyjnie wstaw lewe i prawe poddrzewo
    root.left = sorted_array_to_avl(arr[:mid])
    root.right = sorted_array_to_avl(arr[mid + 1:])

    return root


def array_to_random_bst(arr):
    """Tworzy losowe binarne drzewo szukania z podanej tablicy.

    Args:
        arr (List[int]): Lista kluczy

    Returns:
        Node | None: Korzeń drzewa (lub None w przypadku tablicy pustej)
    """

    if len(arr) == 0:
        return None

    root = Node(arr[0])
    for i in range(1, len(arr)):
        root.insert(arr[i])
    return root

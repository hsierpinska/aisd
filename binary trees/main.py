from Node import Node
import numpy as np
from generating_tree import generate_data
from generating_tree import input_data
from generating_tree import sorted_array_to_avl
from generating_tree import array_to_random_bst
from typing import List
from time import time



arr = None
tree = Node(None)


def fetching_data_step() -> List[int]:
    while True:
        n = input(
            "Chcesz wygenerować losowe dane, czy wpisać z klawiatury?\n 1. Wygenerować dane,\n 2. Wpisać z klawiatury,\n 3. Wyjść z programu.\n")

        if n == '1':
            count = int(input("Jak długa ma być długość tablicy do wygenerowania? Wprowadź liczbę.\n"))
            return generate_data(count)

        elif n == '2':
            count = int(input("Jak długa ma być długość tablicy do wygenerowania? Wprowadź liczbę.\n"))
            return input_data(count)

        elif n == '3':
            exit(0)

        else:
            print("Wprowadź prawidłową liczbę.\n")
            input("Naciśnij Enter, by przejść ponownie do menu...\n")


def generating_tree_step(arr: List[int]) -> Node:
    while True:
        n = input(
            "Wybierz opcję:\n 1. Budowanie losowego drzewa BST\n 2. Budowanie drzewa AVL wyszukiwaniem binarnym\n 3. Wyjście z programu.\n")

        if n == '1':
            root = array_to_random_bst(arr)
            if root:
                print("Zbudowano losowe drzewo BST pomyślnie.")
            return root

        elif n == '2':
            sort = list(np.sort(arr))
            root = sorted_array_to_avl(sort)
            if root:
                print("Zbudowano drzewo AVL pomyślnie.")
            return root

        elif n == '3':
            exit(0)

        else:
            print("Wprowadź prawidłową liczbę")
            input("Naciśnij Enter, by przejść ponownie do menu...\n")


def tree_operations_step(tree: Node) -> Node:
    n = input("Wybierz opcję:\n\n 1. Wyszukanie w drzewie elementu o najmniejszej"
              " i największej wartości i wypisanie ścieżki poszukiwania"
              " (od korzenia do elementu szukanego)\n 2. Usunięcie elementu drzewa"
              " o wartości klucza podanej przez użytkownika"
              " (użytkownik wpisuje ile węzłów chce usunąć i podaje wartości kluczy)\n"
              " 3. Wypisanie elementów preorder\n 4. Wypisanie elementów inorder\n 5. Wypisanie elementów postorder\n"
              " 6. Usunięcie całego drzewa element po elemencie metodą post-order\n"
              " 7. Wypisanie w porządku pre-order podrzewa, ktorego korzeń (klucz) podaje użytkownik\n"
              " 8. Równoważenie drzewa przez rotacje (algorytm DSW)\n 9. Wyjście z programu\n 10. Wypisanie drzewa\n")

    if n == '1':
        print("Wybrano wyszukanie w drzewie elementu o najmniejszej"
              " i największej wartości i wypisanie ścieżki poszukiwania.\n")
        print("Wyszukiwanie najmniejszego elementu:\n")
        start = time()
        tree.find_min(printing=True)
        end = time()
        print("\nZmierzony czas: ", (end - start))
        print("\nWyszukiwanie największego elementu:\n")
        start = time()
        tree.find_max()
        end = time()
        print("\nZmierzony czas: ", (end - start))
        input("Naciśnij Enter, by przejść ponownie do menu...\n")

    elif n == '2':
        print("\nUsuwanie węzłów")
        arr_values = []
        count = int(input("Podaj liczbę węzłów, które chcesz usunąć: "))
        for _ in range(count):
            a = int(input("Podaj wartość dla węzła do usunięcia: "))
            arr_values.append(a)
        print("\nPrzed usunięciem (wypisanie preorderem):")
        tree.preorder_print()
        start = time()
        # tree.delete_nodes(arr_values)
        for i in range(len(arr_values)):
            tree = tree.deleteNode(tree, arr_values[i])
        end = time()
        print("\nPo usunięciu (wypisanie preorderem):")
        tree.preorder_print()
        print("\nZmierzony czas: ", (end - start))
        input("Naciśnij Enter, by przejść ponownie do menu...\n")

    elif n == '3':
        print("\nWypisanie elementów w porządku preorder")
        start = time()
        tree.preorder_print()
        end = time()
        print("\nZmierzony czas: ", (end - start))
        input("Naciśnij Enter, by przejść ponownie do menu...\n")

    elif n == "4":
        print("\nWypisanie elementów w porządku inorder")
        start = time()
        tree.inorder_print()
        end = time()
        print("\nZmierzony czas: ", (end - start))
        input("Naciśnij Enter, by przejść ponownie do menu...\n")

    elif n == '5':
        print("\nWypisanie elementów w porządku postorder")
        start = time()
        tree.postorder_print()
        end = time()
        print("\nZmierzony czas: ", (end - start))
        input("Naciśnij Enter, by przejść ponownie do menu...\n")

    elif n == '6':
        start = time()
        print("\nUsunięcie całego drzewa element po elemencie metodą postorder")
        tree.postorder_delete()
        end = time()
        print("\nZmierzony czas: ", (end - start))
        input("Naciśnij Enter, by przejść ponownie do menu...\n")

    elif n == '7':

        print("\nWypisanie w porządku pre-order podrzewa, ktorego korzeń (klucz) podaje użytkownik")
        key = input("Podaj korzeń (klucz) poddrzewa, które chcesz wypisać: ")
        start = time()
        tree.print_subtree_preorder(int(key))
        end = time()
        print("\nZmierzony czas: ", (end - start))
        input("Naciśnij Enter, by przejść ponownie do menu...\n")

    elif n == '8':
        start = time()
        print("\nRównoważenie drzewa algorytmem DSW\n")
        print("Wypisanie elementów drzewa metodą preorder przed równoważeniem:")
        tree.preorder_print()
        tree = tree.balance_dsw()
        print("Wypisanie elementów drzewa metodą preorder po równoważeniu:")
        found = tree.preorder_print()
        if found:
            end = time()
            print("\nZmierzony czas: ", (end - start))
        input("Naciśnij Enter, by przejść ponownie do menu...\n")

    elif n == '9':
        exit(0)

    elif n == "10":
        tree.display()
        input("Naciśnij Enter, by przejść ponownie do menu...\n")

    else:
        print("Wprowadź prawidłową liczbę")
        input("Naciśnij Enter, by przejść ponownie do menu...\n")

    return tree


while True:
    if not arr:
        arr = fetching_data_step()
    if tree.is_empty():
        tree = generating_tree_step(arr)

    tree = tree_operations_step(tree)

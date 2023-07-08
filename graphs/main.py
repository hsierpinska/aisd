from typing import List
from Graph import Graph
from read import read_file, read_user

graph = None


def fetching_data_step() -> Graph:
    while True:
        n = input(
            "Chcesz wczytać dane z pliku, czy wpisać z klawiatury?\n 1. Wczytać dane z pliku,\n 2. Wpisać z klawiatury,\n 3. Wyjść z programu.\n")

        if n == '1':
            filename = str(input("Podaj nazwę pliku\n"))
            graph = read_file(filename)
            if graph:
                print("Wygenerowano graf pomyślnie.")
                input("Naciśnij Enter, by przejść do menu...\n")
            return graph
        elif n == '2':
            graph = read_user()
            if graph:
                print("Wygenerowano graf pomyślnie.")
                input("Naciśnij Enter, by przejść do menu...\n")
            return graph


        elif n == '3':
            exit(0)

        else:
            print("Wprowadź prawidłową liczbę.\n")
            input("Naciśnij Enter, by przejść ponownie do menu...\n")


def graph_operations_step(graph):
    while True:

        n = input(
            "Wybierz opcję:\n1. Sortowanie topologiczne listy następników z użyciem algorytmu Kahna"
            "\n2. Sortowanie topologiczne macierzy sąsiedztwa z użyciem algorytmu Kahna"
            "\n3. Sortowanie topologicznie listy następników z użyciem algorytmu Tarjana"
            "\n4. Sortowanie topologicznie macierzy sąsiedztwa z użyciem algorytmu Tarjana"
            "\n5. Wypisanie listy następników"
            "\n6. Wypisanie macierzy sąsiedztwa"
            "\n7. Wyjście z programu\n")

        if n == '1':
            print("\nWybrano sortowanie topologiczne listy następników z użyciem algorytmu Kahna."
                  "\nPosortowana lista:")
            graph.kahn_ln()
            input("Naciśnij Enter, by przejść ponownie do menu...\n")

        elif n == '2':
            print("\nWybrano sortowanie topologiczne macierzy sąsiedztwa z użyciem algorytmu Kahna."
                  "\nPosortowana lista:")

            graph.kahn_ms()
            input("Naciśnij Enter, by przejść ponownie do menu...\n")

        elif n == '3':
            print("\nWybrano sortowanie topologicznie listy następników z użyciem algorytmu Tarjana.")
            vertex = int(input("\nWpisz wierzchołek, od którego chcesz rozpocząć algorytm: "))
            if x := graph.tarjan_ln(vertex):
                if graph.zero:
                    print("\nPosortowana lista:")
                    print(x)
                else:
                    x.remove(0)
                    print("\nPosortowana lista:")
                    print(x)
            input("Naciśnij Enter, by przejść ponownie do menu...\n")

        elif n == '4':
            print("\nWybrano sortowanie topologicznie macierzy sąsiedztwa z użyciem algorytmu Tarjana.")
            vertex = int(input("\nWpisz wierzchołek, od którego chcesz rozpocząć algorytm: "))
            if y := graph.tarjan_ms(vertex):
                if graph.zero:
                    print("\nPosortowana lista:")
                    print(y)
                else:
                    y.remove(0)
                    print("\nPosortowana lista:")
                    print(y)
            input("Naciśnij Enter, by przejść ponownie do menu...\n")

        elif n == '5':
            print("\nWybrano wypisanie listy następników."
                  "\nLista następników:")
            graph.print_list()
            input("Naciśnij Enter, by przejść ponownie do menu...\n")

        elif n == '6':
            print("\nWybrano wypisanie macierzy sąsiedztwa."
                  "\nMacierz sąsiedztwa:")
            graph.print_adj_matrix()
            input("Naciśnij Enter, by przejść ponownie do menu...\n")

        elif n == '7':
            exit(0)

        else:
            print("Wprowadź prawidłową liczbę.\n")
            input("Naciśnij Enter, by przejść ponownie do menu...\n")


while True:
    if not graph:
        graph = fetching_data_step()
    else:
        graph_operations_step(graph)

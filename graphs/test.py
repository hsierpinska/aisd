import numpy as np
import matplotlib.pyplot as plt
from read import read_file, read_user, generate_dag
import timeit

# Wykonaj wykresy t=f(n) zależności czasu obliczeń t od liczby n wierzchołków w grafie (jeden wykres dla każdej
# reprezentacji maszynowej grafu). Na każdym wykresie przedstaw 2 krzywe – po jednej krzywej dla każdej metody
# sortowania topologicznego. Wykonaj 2 wykresy w skali logarytmicznej (jeden wykres dla każdej metody sortowania
# topologicznego) t=f(n) zależności czasu obliczeń t od liczby n wierzchołków w grafie. Na każdym wykresie przedstaw
# po jednej krzywej dla każdej reprezentacji maszynowej grafu. Opisz zalety i wady każdej reprezentacji grafu z
# punktu widzenia ich zastosowania w zaimplementowanych algorytmach.

arr_kahn = []  # czas operacji grafu gdzie indeks odpowiada liczbie elementów
arr_tarjan = []


def create_plot(arr, arr2=None, title=None):
    """

    Args:


        arr: Lista z czasami operacji
        arr2: Lista z czasami operacji, ale druga
        title: Tytuł wykresu

    Returns:

    """

    fig, ax = plt.subplots()
    ax.plot(np.arange(len(arr)), arr, label='Tarjan_ms')
    if arr2:
        ax.plot(np.arange(len(arr2)), arr2, label='Tarjan_ln')
    plt.yscale('log')
    plt.legend(loc="upper left")
    ax.set_xlabel('Elementy - n')
    ax.set_ylabel('Czas w nanosekundach - t')
    if title:
        ax.set_title(title)
    plt.show()


vertex = None
# graph1 = generate_dag(1)
# graph1.print_list()
for i in range(4, 1004):
    a = str(i)
    graph = generate_dag(i)[1]
    print(i)
    for e in range(len(graph.list)):
        if len(graph.list[e]) != 0:
            vertex = graph.list[e][0]

    if vertex:
        time1 = timeit.timeit('graph.tarjan_ms(vertex)',
                              setup='\n'
                                    'from __main__ import graph, vertex\n'
                                    'a=' + a, number=1)
        time2 = timeit.timeit('graph.tarjan_ln(vertex)',
                              setup='\n'
                                    'from __main__ import graph, vertex\n'
                                    'a=' + a, number=1)
        arr_kahn.append(time1)
        arr_tarjan.append(time2)

arr_kahn = [sum(arr_kahn[i:i + 10]) / 10 for i in
            range(0, len(arr_kahn))]
arr_tarjan = [sum(arr_tarjan[i:i + 10]) / 10 for i in
              range(0, len(arr_tarjan))]
create_plot(arr_kahn, arr_tarjan, "Porównanie metod sortowania topologicznego tarjan_ms, tarjan_ln")
# create_plot(arr_nanoseconds_avl, arr_nanoseconds_bst, "Budowanie drzewa")

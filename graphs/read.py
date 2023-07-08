# Program powinien mieć możliwość wczytywania danych z klawiatury oraz z pliku tekstowego zawierającego graf zapisany
# w postaci listy krawędzi, gdzie para liczb w pierwszej linii to informacja o liczbie wierzchołków i liczbie
# krawędzi, a pary w kolejnych liniach to pary wierzchołków połączonych łukiem. Spacja jest separatorem liczb w
# pojedynczej linii.
from matplotlib import pyplot as plt

from Graph import Graph
import random
import networkx as nx


def read_file(filename: str) -> Graph:
    '''

    :param filename: Nazwa pliku czytanego.
    Przyjmuje, że para liczb w pierwszej linii to liczba wierzchołków i krawędzi,
    a pary w kolejnych liniach to pary wierzchołków połączonych łukiem.
    Spacja jest separatorem.
    :return: Graf z wierzchołkami z pliku
    '''
    file = open(filename, 'r')
    f1 = [[int(x) for x in line.rstrip().split()] for line in file]
    graph = Graph(int(f1[0][0]) + 1)  # liczba wierzchołków
    [graph.add_edge(f1[i][0], f1[i][1]) for i in range(1, len(f1))]
    return graph


def read_user() -> Graph:
    '''
    Wczytuje dane z klawiatury i generuje graf.
    :return: Zwraca graf, a jeśli podane są dane w nieprawidłowym formacie, zwraca False
    '''
    try:
        vertices = int(input("Wprowadź liczbę wierzchołków: ")) + 1
        edges = int(input("Wprowadź liczbę krawędzi: "))
        graph = Graph(vertices)

        for i in range(int(edges)):
            x = [int(i) for i in input("Wprowadź wartości wierzchołków, pomiędzy którymi ma się znaleźć łuk "
                                       "[separowane spacją]: ").split(" ")]
            print(x)
            graph.add_edge(x[0], x[1])
        return graph
    except ValueError:
        raise ValueError("Nieprawidłowy format danych")


# Wygeneruj proste grafy skierowane acykliczne o n wierzchołkach i współczynniku nasycenia krawędziami równym 50% (
# oznacza to, że liczba krawędzi grafu wynosi 50% z n(n-1)/2) dla 10-15 różnych wartości n z przedziału <100,
# k> (k należy je dobrać eksperymentalnie tak, aby możliwe było wykonanie pomiarów i aby jego wartość była możliwie
# duża; proponowane k=1500).

def generate_dag(n: int):
    # Create an empty directed graph
    graph = None
    G = nx.gnp_random_graph(n, 0.5, directed=True)
    DAG = nx.DiGraph([(u, v,) for (u, v) in G.edges() if u < v])
    graph = Graph(n)
    for u, v in DAG.edges():
        graph.add_edge(u, v)
    A = nx.adjacency_matrix(DAG)
    AM = A.toarray().tolist()  # 1 for outgoing edges
    while len(AM) != n:
        AM = generate_dag(n)[0]



    return AM, graph

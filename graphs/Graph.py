# Zaimplementuj 2 algorytmy sortowania topologicznego wierzchołków grafu: (i) z wykorzystaniem procedury
# przechodzenia w głąb (algorytm Tarjana) i (ii) z usuwaniem wierzchołków o zerowym stopniu wejściowym (algorytm
# Kahna). Każdy z algorytmów należy zaimplementować na dwóch reprezentacjach maszynowych grafu: (a) macierz
# sąsiedztwa, (b) lista następników.
# Razem należy zaimplementować algorytmy: Tarjan_ms, Tarjan_ln, Kahn_ms, Kahn_ln.
# Algorytmy powinny wykrywać cykle w grafie wejściowym. W wersji przedstawianej na zaliczenie w przypadku
# znalezienia cyklu, należy przerwać sortowanie i wyświetlić komunikat: „Graf zawiera cykl. Sortowanie niemożliwe.”
# Program powinien umożliwiać wystartowanie algorytmu Tarjana z wierzchołka podanego przez użytkownika (ta wersja
# będzie wykorzystywana tylko podczas zaliczania programu na zajęciach) lub z wierzchołka domyślnego – o zerowym
# stopniu wejściowym (ta wersja będzie wykorzystywana do testów).
import numpy as np


class Graph:
    """
    Klasa reprezentująca grafy
    """

    def __init__(self, vertices):
        '''Generowanie pustej macierzy sąsiedztwa, listy następników jako reprezentacji grafu
        :param vertices: Liczba wierzchołków w grafie
        '''
        self.vertices = vertices
        self.adj_matrix = [[0 for i in range(vertices)] for j in range(vertices)]
        # self.graph_matrix = [[0 for i in range(vertices)] for j in range(vertices+3)]
        self.list = [[] for i in range(vertices)]
        self.visited = [False] * (vertices)
        self.zero = False
        self.edges = 0

    def add_edge(self, u, v):
        '''
        Funkcja dodająca łuki pomiędzy wierzchołkami
        :param u: Wierzchołek u
        :param v: Wierzchołek v

        :return:
        '''
        if u == 0 or v == 0:
            self.zero = True
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = -1
        self.list[u].append(v)
        self.list[u].sort()
        self.edges += 1
        # self.graph_matrix[u][self.vertices+1] = v
        # self.graph_matrix[u][v] =


    def print_adj_matrix(self):
        print(np.matrix.view(np.matrix([row[1:] for row in self.adj_matrix[1:]])))

    def print_list(self):
        for i in range(self.vertices):
            print(f"{i}: ", end="")
            if len(self.list[i]) > 0:
                print(f"{self.list[i][0]}", end="")
                for j in self.list[i][1:]:
                    print(f" -> {j}", end="")
            print()

    def delete_vertex(self, vertex):
        '''
        Usuwa wierzchołek i jego połączenia z innymi wierzchołkami
        z listy następników, a także z macierzy sąsiedztwa
        :param vertex: Wierzchołek do usunięcia
        :return:
        '''
        self.list[vertex].clear()
        for x in self.list:
            try:
                x.remove(vertex)
            except ValueError:
                continue
        for i in range(self.vertices):
            for j in range(self.vertices):
                if i == vertex or j == vertex:
                    self.adj_matrix[i][j] = 0

    def kahn_ln(self):

        degree = [sum(1 for i in range(self.vertices) if j in self.list[i]) for j in range(self.vertices)]
        queue = [i for i in range(0, len(degree)) if degree[i] == 0]
        count = 0
        top_order = []
        while queue:
            u = queue.pop(0)
            top_order.append(u)
            for i in self.list[u]:
                degree[i] -= 1
                if degree[i] == 0:
                    queue.append(i)
            count += 1
        if count != self.vertices:
            print("Graf zawiera cykl. Sortowanie niemożliwe.")
        else:
            if self.zero:
                print(top_order)
            else:
                top_order.remove(0)
                print(top_order)

    def kahn_ms(self):

        degree = [sum(1 for i in range(self.vertices) if self.adj_matrix[i][j] == 1) for j in range(self.vertices)]
        queue = [i for i in range(0, len(degree)) if degree[i] == 0]
        count = 0
        top_order = []
        while queue:
            u = queue.pop(0)
            top_order.append(u)
            for i in range(self.vertices):
                if self.adj_matrix[u][i] == 1:
                    degree[i] -= 1
                    if degree[i] == 0:
                        queue.append(i)

            count += 1
        if count != self.vertices:
            print("Graf zawiera cykl. Sortowanie niemożliwe.")
        else:
            if self.zero:
                print(top_order)
            else:
                top_order.remove(0)
                print(top_order)

    def tarjan_ln(self, start=None, L=[], C=[]):
        """Algorytm Tarjana.

            Oparty na DFS. Operuje listą następników.

            Args:
                start (int, optional): Wierzchołek startowy. W przypadku domyślnym znajduje pierwszy wierzchołek o zerowym stopniu wejściowym.
                L (list, don't use): Wierzchołki posortowane topologicznie. Defaults to [].
                C (list, don't use): Tablica kolorów wierzchołków. Defaults to [].

            Returns:
                list: Wierzchołki posortowane topologicznie.
            """
        if not C:
            C = ['b' for _ in range(self.vertices)]

        if start == None:
            for i in range(self.vertices):
                if i not in self.list and C[i] == 'b':
                    start = i
                    break

        u = start
        C[u] = 'sz'
        for successor in self.list[u]:
            if C[successor] == 'b':
                L = self.tarjan_ln(successor, C=C, L=L)
                if L is None:
                    return
            elif C[successor] in ('sz'):
                print("Graf zawiera cykl. Sortowanie niemożliwe.")
                return

        C[u] = 'cz'
        L.insert(0, u)
        # jeśli u nie ma szarego poprzednika i w grafie są jeszcze białe wierzchołki
        if 'sz' not in C and 'b' in C:
            L = self.tarjan_ms(L=L, C=C)
        return L

    def tarjan_ms(self, start=None, L=[], C=[]):
        """Algorytm Tarjana.

        Oparty na DFS. Operuje macierzą sąsiedztwa.

        Args:
            start (int, optional): Wierzchołek startowy. W przypadku domyślnym znajduje pierwszy wierzchołek o zerowym stopniu wejściowym.
            L (list, don't use): Wierzchołki posortowane topologicznie. Defaults to [].
            C (list, don't use): Tablica kolorów wierzchołków. Defaults to [].

        Returns:
            list: Wierzchołki posortowane topologicznie.
        """
        if not C:
            C = ['b' for _ in range(self.vertices)]

        if start == None:
            for (i, row) in enumerate(self.adj_matrix):
                if -1 not in row and C[i] == 'b':
                    start = i
                    break

        u = start
        C[u] = 'sz'

        for (successor, edge) in enumerate(self.adj_matrix[u]):
            if edge == 1 and C[successor] == 'b':
                L = self.tarjan_ms(successor, L=L, C=C)
                if L is None:
                    return

            elif edge == 1 and C[successor] in ('sz'):
                print("Graf zawiera cykl. Sortowanie niemożliwe.")
                return

        C[u] = 'cz'
        L.insert(0, u)

        if 'sz' not in C and 'b' in C:
            L = self.tarjan_ms(L=L, C=C)
        return L



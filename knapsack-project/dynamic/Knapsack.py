# c – udźwig plecaka
# n – liczba przedmiotów w zbiorze
# xi – zmienna decyzyjna (czy i-ty przedmiot jest w zbiorze)
# pi – wartość i-tego przedmiotu
# wi – masa i-tego przedmiotu

class Knapsack:
    """Klasa reprezentująca plecak z przedmiotami o udźwigu c"""
    def __init__(self, arr, c):
        self.list = arr
        self.c = c

    def extract(self, bin_num):
        """Zwraca liczbę binarną jako tablica elementów w systemie dziesiętnych,
        ich suma jest równa liczbie (binarnej) podanej w parametrze """
        a = [i + 1 for i, n in enumerate(bin_num[::-1]) if n == "1"]
        return a

    def summary_size(self, bag):
        # zakłada jako input liczby od 1 do n
        sum_m = 0
        for el in bag:
            sum_m += self.list[el - 1][0]
        return sum_m

    def summary_value(self, bag):
        # zakłada jako input liczby od 1 do n
        sum_v = 0
        for el in bag:
            sum_v += self.list[el - 1][1]
        return sum_v

    def knapsack_brute_force(self):

        """
        Algorytm siłowy dla plecaka
        arr - lista z przedmiotami
        c - udźwig plecaka (maksymalna masa w środku)
        :return:
        """
        c = self.c
        arr = list(self.list)
        n = len(arr)
        fmax = 0
        solution = 0
        for i in range(1, 2 ** n):
            w_i = 0  # suma mas w obecnej iteracji
            f_i = 0  # suma wartości przedmiotów
            bin_num = format(i, 'b')
            curr_sol = self.extract(bin_num)
            w_i = sum(arr[el - 1][0] for el in curr_sol)
            if w_i <= c:
                f_i = sum(arr[el - 1][1] for el in curr_sol)
                if f_i > fmax:
                    fmax = f_i
                    solution = curr_sol
        return solution


    def sorter(self, arr):
        return sorted(arr, key=lambda n: n[1] / n[0], reverse=True)

    def knapsack_greedy_3(self):
        """Algorytm zachłanny"""
        c = self.c
        arr = list(self.list)
        og_arr = list(arr)
        a = []
        bag = []
        n = len(arr)
        arr = self.sorter(arr)
        for i in range(n):
            if c < 0:
                break
            if arr[i][0] <= c:
                bag.append(arr[i])
                c -= arr[i][0]
        for el in bag:
            a.append(og_arr.index(el) + 1)

        return a

    def knapsack_dynamic(self):
        """Algorytm dynamiczny, zwraca binarną listę i największą wartość"""
        c = self.c
        arr = list(self.list)
        n = len(arr)
        v = [[0] * (c + 1) for _ in range(n + 1)]
        x = []
        for i in range(1, n + 1):
            for j in range(c + 1):
                w_i, p_i = arr[i - 1]

                if w_i > j:
                    v[i][j] = v[i - 1][j]
                else:
                    v[i][j] = max(v[i - 1][j], v[i - 1][j - w_i] + p_i)
        w, k = len(v) - 1, len(v[0]) - 1
        x = [0 for _ in arr]
        for i in range(n)[::-1]:
            if v[w][k] > v[w - 1][k]:
                x[i] = 1
                k -= arr[i][0]
            w -= 1
        return x, v[n][c]


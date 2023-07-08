# Wykonaj dla każdego algorytmu wykres t=f(n) zależności czasu obliczeń t od liczby n przedmiotów,
# przy stałej pojemności plecaka b.
from Knapsack import Knapsack
import random


def generate_knapsack(n, c):
    knapsack = []
    for i in range(n):
        knapsack.append([random.randint(1, 1000), random.randint(1, 1000)])
    knapsack = Knapsack(knapsack, c)
    return knapsack




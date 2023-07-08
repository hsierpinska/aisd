from Knapsack import Knapsack


def read_file(filename: str):
    '''

    :param filename: Nazwa pliku czytanego.
    Przyjmuje, że para liczb w pierwszej linii to liczba przedmiotów i udźwig plecaka,
    a pary w kolejnych liniach to kolejno waga i wartość poszczególnego przedmiotu.
    Spacja jest separatorem.
    :return: Plecak
    '''
    try:
        with open(filename, 'r') as file:
            f1 = [[int(x) for x in line.rstrip().split()] for line in file]
            n, c = f1[0]
            f1 = f1[1:]
            if n<0 or c<0:
                raise ValueError("Złe dane")
            for element in f1:
                if element[0]<0 or element[1]<0:
                    raise ValueError("Złe dane")
            if len(f1) == n:
                knapsack = Knapsack(f1, c)
                return knapsack
            else:
                print("Wprowadzono złą liczbę przedmiotów: ", n, " =/= ", len(f1))
    except ValueError:
        raise ValueError("Nieprawidłowy format danych")




def read_user():
    '''
    Wczytuje dane z klawiatury i generuje plecak z przedmiotami.
    :return: Zwraca plecak, a jeśli podane są dane w nieprawidłowym formacie, informuje o tym
    '''

    try:
        n = int(input("Wprowadź liczbę przedmiotów: "))
        c = int(input("Wprowadź udźwig plecaka: "))

        a = []
        if n < 0 or c < 0:
            raise ValueError("Złe dane")
        for i in range(int(n)):
            x = [int(i) for i in input("Wprowadź wagi przedmiotów oraz ich wartości"
                                       "[separowane spacją]: ").split(" ")]
            if x[0]<0 or x[1]<0:
                raise ValueError("Złe dane")

            a.append(x)
        knapsack = Knapsack(a, c)
        return knapsack

    except ValueError:
        raise ValueError("Nieprawidłowy format danych")


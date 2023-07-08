from Knapsack import Knapsack
from read import read_file, read_user

knapsack = None


def fetching_data_step() -> Knapsack:
    while True:
        n = input(
            "Chcesz wczytać dane z pliku, czy wpisać z klawiatury?\n 1. Wczytać dane z pliku,\n 2. Wpisać z klawiatury,\n 3. Wyjść z programu.\n")

        if n == '1':
            filename = str(input("Podaj nazwę pliku\n"))
            knapsack = read_file(filename)
            if knapsack:
                print("Wygenerowano plecak pomyślnie.")
                input("Naciśnij Enter, by przejść do menu...\n")
            return knapsack
        elif n == '2':
            knapsack = read_user()
            if knapsack:
                print("Wygenerowano plecak pomyślnie.")
                input("Naciśnij Enter, by przejść do menu...\n")
            return knapsack


        elif n == '3':
            exit(0)

        else:
            print("Wprowadź prawidłową liczbę.\n")
            input("Naciśnij Enter, by przejść ponownie do menu...\n")


def knapsack_operations_step(knapsack):
    while True:
        n = input(
            "Wybierz opcję:\n1. Algorytm programowania dynamicznego AD"
            "\n2. Algorytm zachłanny AZ (sortowanie po współczynniku opłacalności: wartość na jednostkę masy)"
            "\n3. Algorytm siłowy AB"
            "\n4. Pokaż listę przedmiotów"
            "\n5. Wyjście z programu\n")

        if n == '1':
            print("\nWybrano algorytm programowania dynamicznego AD")
            print("Wybrane przedmioty: ")
            x = knapsack.knapsack_dynamic()
            print("Zmienna decyzyjna: ", x[0])
            print("Maksymalna wartość funkcji celu: ", x[1])
            a = [i+1 for i in range(len(x[0])) if x[0][i]==1]
            print("Wybrane przedmioty do plecaka: ", a)
            print("Sumaryczna masa przedmiotów plecaka: ", knapsack.summary_size(a))
            input("Naciśnij Enter, by przejść ponownie do menu...\n")

        elif n == '2':
            print("\nWybrano algorytm zachłanny AZ")
            a = knapsack.knapsack_greedy_3()
            print("Wybrane przedmioty do plecaka: ", a)
            print("Sumaryczna masa przedmiotów plecaka: ", knapsack.summary_size(a))
            print("Sumaryczna wartość przedmiotów plecaka: ", knapsack.summary_value(a))
            input("Naciśnij Enter, by przejść ponownie do menu...\n")

        elif n == '3':
            print("\nWybrano algorytm siłowy AB.")
            a = knapsack.knapsack_brute_force()
            print("Wybrane przedmioty do plecaka: ", a)
            print("Sumaryczna masa przedmiotów plecaka: ", knapsack.summary_size(a))
            print("Sumaryczna wartość przedmiotów plecaka: ", knapsack.summary_value(a))

            input("Naciśnij Enter, by przejść ponownie do menu...\n")

        elif n == '4':
            print(knapsack.list)
            input("Naciśnij Enter, by przejść do menu...\n")
        elif n == '5':
            exit(0)

        else:
            print("Wprowadź prawidłową liczbę.\n")
            input("Naciśnij Enter, by przejść ponownie do menu...\n")


while True:
    if not knapsack:
        knapsack = fetching_data_step()
    else:
        knapsack_operations_step(knapsack)

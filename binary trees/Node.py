from math import floor, log2


class Node:

    def __init__(self, key: int):
        self.left = None
        self.right = None
        self.key = key

    def insert(self, key: int):
        """Wstawia klucz do drzewa

        Args:
            key (int): Wartość klucza
        """
        if key < self.key:
            if self.left is None:
                self.left = Node(key)
            else:
                self.left.insert(key)
        elif key > self.key:
            if self.right is None:
                self.right = Node(key)
            else:
                self.right.insert(key)
        else:  # key == self.key, czyli Node już istnieje
            return

    def inorder_print(self, printing=True):
        """Wypisanie wszystkich elementów drzewa w porządku rosnącym (in-order).
        """

        if self.left:
            self.left.inorder_print(printing)
        if printing:
            print("Węzeł: ", self.key)
        if self.right:
            self.right.inorder_print(printing)

    def preorder_print(self):  #
        """Wypisanie wszystkich elementów drzewa w porządku pre-order.
        """

        print("Węzeł: ", self.key)
        if self.left:
            self.left.preorder_print()
        if self.right:
            self.right.preorder_print()

    def postorder_print(self):  #
        """Wypisanie wszystkich elementów drzewa w porządku post-order.
        """
        if self.left:
            self.left.postorder_print()
        if self.right:
            self.right.postorder_print()
        print("Węzeł: ", self.key)

    def find_min(self, printing, is_root=True):
        """Wyszukanie w drzewie elementu o najmniejszej wartości i wypisanie ścieżki poszukiwania (od korzenia do elementu szukanego).
        Args:
            is_root: Określa, czy bieżący węzeł jest korzeniem drzewa
            printing: Określa, czy wypisywać ścieżkę poszukiwania

        Returns:
            int: Minimalna wartość drzewa

        """
        if printing:
            if is_root:
                print("Korzeń: ", self.key)
            else:
                print("Węzeł: ", self.key)

        if self.left is None:
            if printing:
                print("Minimalna wartość znaleziona: ", self.key)
            return self.key

        return self.left.find_min(printing, is_root=False)

    def find_max(self, is_root=True):
        """Wyszukanie w drzewie elementu o największej wartości i wypisanie ścieżki poszukiwania (od korzenia do elementu szukanego).

        Returns:
            int: Maksymalna wartość drzewa
        """

        if is_root:
            print("Korzeń: ", self.key)
        else:
            print("Węzeł: ", self.key)

        if self.right is None:
            print("Maksymalna wartość znaleziona: ", self.key)
            return self.key

        return self.right.find_max(is_root=False)

    def search(self, key: int):
        """Funkcja pomocnicza do szukania poddrzewa.

        Args:
            key (int): Wartość szukana

        Returns:
            Node: Poddrzewo z podanym kluczem korzenia
        """
        if key < self.key:
            if self.left is None:
                return False
            else:
                return self.left.search(key)
        elif key > self.key:
            if self.right is None:
                return False
            else:
                return self.right.search(key)
        else:
            return self

    def print_subtree_preorder(self, key: int):
        """Wypisanie w porządku pre-order podrzewa, ktorego korzeń (klucz) podaje użytkownik.

        Args:
            key (int): _description_
        """
        subtree = self.search(key)
        if subtree:
            subtree.preorder_print()
        else:
            print("Nie znaleziono podanego klucza w drzewie.")
            return None

    def postorder_delete(self):
        """Usunięcie całego drzewa element po elemencie metodą post-order (wypisz element przed usunięciem).
        """
        if self.left:
            self.left.postorder_delete()
        if self.right:
            self.right.postorder_delete()
        if self.key is not None:
            print("Usuwany element: ", self.key)
        self.key = None

    def deleteNode(self, root, key: int):
        '''Usuwanie węzłów drzewa o określonym kluczu

        Args:
            root (Node): węzeł
            key (int): klucz węzła, który chcemy usunąć
        Returns:
            root (Node): drzewo z usuniętym węzłem
        '''
        if not root:
            return None
        if root.key == key:

            # liść
            if not root.left and not root.right:
                return None
            if not root.left and root.right:  # ma prawego lub lewego potomka
                return root.right
            if not root.right and root.left:
                return root.left
            # ma oboje potomków
            successor = root.right.find_min(printing=False)
            root.key = successor
            root.right = self.deleteNode(root.right, root.key)
        elif root.key > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

    def is_empty(self):
        if self.key is not None:
            return False
        if self.left is not None and not self.left.is_empty():
            return False
        if self.right is not None and not self.right.is_empty():
            return False
        return True

    def __len__(self) -> int:
        """Zwraca liczbę węzłów w poddrzewie o korzeniu w aktualnym węźle.

        Returns:
            int: Liczba węzłów w danym poddrzewie
        """
        count = 1
        if self.left:
            count += len(self.left)
        if self.right:
            count += len(self.right)
        return count

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def right_rotate(self):
        """Dokonuje prawej rotacji na podanym węźle.

        Raises:
            ValueError: Brak lewego dziecka

        Returns:
            Node: Nowy korzeń poddrzewa
        """
        if not self.left:
            raise ValueError("Nie można wykonać prawej rotacji bez lewego dziecka.")

        root = self
        pivot = self.left

        pivot.right, root.left = root, pivot.right

        return pivot

    def left_rotate(self):
        """Dokonuje lewej rotacji na podanym węźle.

        Raises:
            ValueError: Brak prawego dziecka

        Returns:
            Node: Nowy korzeń poddrzewa
        """
        if not self.right:
            raise ValueError("Nie można wykonać lewej rotacji bez prawego dziecka.")

        root = self
        pivot = self.right

        pivot.left, root.right = root, pivot.left

        return pivot

    def to_vine(self):
        """Zamienia poddrzewo w kręgosłup.

        Returns:
            Node: Korzeń poddrzewa
        """
        curr = self
        while curr.left:
            curr = curr.right_rotate()

        if curr.right:
            curr.right = curr.right.to_vine()
        return curr

    def _rrr(self, n: int):
        """rrr robi jedną rotację w lewo, a następnie wywołuję sam siebie na swoim prawym dziecku, ale nie więcej razy niż n.

        Wykorzystywane wyłącznie w algorytmie DSW.

        Args:
            n (int): Liczba rotacji

        Returns:
            Node: Korzeń poddrzewa
        """
        curr = self

        if curr.right and n:
            curr = curr.left_rotate()

            if curr.right and n:
                curr.right = curr.right._rrr(n - 1)

        return curr

    def balance_dsw(self):
        if self.is_balanced():
            return self

        """Równoważy poddrzewo za pomocą algorytmu DSW.

        Returns:
            Node: Nowy korzeń poddrzewa
        """
        root = self.to_vine()

        n = len(root)
        m = 2 ** floor(log2(n + 1)) - 1

        # 2. faza - balans
        root = root._rrr(n - m)
        while m > 1:
            m //= 2
            root = root._rrr(m)

        return root

    def is_balanced(self):
        def check_height(node):
            if not node:
                return 0
            left_height = check_height(node.left)
            if left_height == -1:
                return -1
            right_height = check_height(node.right)
            if right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1

        return check_height(self) != -1

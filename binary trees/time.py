
from generating_tree import array_to_random_bst, sorted_array_to_avl, generate_data
import numpy as np
import cProfile
arr_balance_avl = []
arr_balance_bst = []
for i in range(1, 20):
    print(i)
    avl_tree = sorted_array_to_avl(np.sort(generate_data(i)))
    bst_tree = array_to_random_bst(generate_data(i))
    avl_tree.balance_dsw()
    bst_tree.balance_dsw()


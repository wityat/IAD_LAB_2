# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

import numpy as np
from sklearn.datasets import load_iris


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from sklearn.cluster import AgglomerativeClustering

from scipy.spatial import distance
from scipy.cluster import hierarchy
from sklearn.cluster import AgglomerativeClustering

from scipy.cluster.hierarchy import ward, fcluster, linkage, dendrogram
from scipy.spatial.distance import pdist, cdist, squareform
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import AgglomerativeClustering

X = [[0, 0], [0, 1], [1, 0],
     [0, 4], [0, 3], [1, 4],
     [4, 0], [3, 0], [4, 1],
     [4, 4], [3, 4], [4, 3]]

# Z = ward(l := pdist(X))

# print(l)

X = load_iris(return_X_y=False)
# print(X["data"])
iris = pd.DataFrame(X['data'], columns=X['feature_names'])
l = cdist(X["data"], X["data"])
# print(l)
# print(squareform(l))
# y = squareform(l)
# print(np.where(y == 0.42267224))
#
# Z1 = linkage(l, method="single")
# print(Z1)


A = np.array([[0.1, 2.5],
              [1.5, .4],
              [0.3, 1],
              [1, .8],
              [0.5, 0],
              [0, 0.5],
              [0.5, 0.5],
              [2.7, 2],
              [2.2, 3.1],
              [3, 2],
              [3.2, 1.3]])


# l = cdist(A, A)


def merge(dict_d_matrix: dict, taboo_cl: list, result: list, len_n: int, method="min"):
    x_ = (0, 0, float("inf"))
    for i, d in dict_d_matrix.items():
        for j, x in enumerate(d):
            if x < x_[2] and i != j and j not in taboo_cl and i not in taboo_cl:
                x_ = i, j, x
    taboo_cl.append(x_[0])
    taboo_cl.append(x_[1])
    dict_d_matrix[len(dict_d_matrix)] = np.array([])

    count_old_cl = 0
    count_old_cl += result[x_[0] - len_n][3] if x_[0] >= len_n else 1
    count_old_cl += result[x_[1] - len_n][3] if x_[1] >= len_n else 1
    result.append([*x_, count_old_cl])

    # if method == "mean":
    #     cl_nums = [x_[0], x_[1]]
    #     c = result[-1][3]
    #     c -= 2
    #     while c > 0:
    #         if x_[0] >= len_n:
    #             result[x_[0] - len_n][0]
    #             result[x_[0] - len_n][1]
    #         result[x_[1] - len_n][0]
    #         result[x_[1] - len_n][1]

    for n, i in enumerate(dict_d_matrix[x_[0]]):
        dict_d_matrix[len(dict_d_matrix) - 1] = np.append(dict_d_matrix[len(dict_d_matrix) - 1],
                                                          getattr(np, method)([dict_d_matrix[x_[1]][n], i]))
    dict_d_matrix[len(dict_d_matrix) - 1] = np.append(dict_d_matrix[len(dict_d_matrix) - 1], 0.0)

    for i, d in dict_d_matrix.items():
        if i == len(dict_d_matrix) - 1:
            break
        dict_d_matrix[i] = np.append(d, dict_d_matrix[len(dict_d_matrix) - 1][i])

    return dict_d_matrix, taboo_cl, result


Z1 = linkage(iris, method="single")
print(list(Z1))


def linkage(d_matrix, method="min"):
    d_matrix = squareform(pdist(d_matrix))
    dict_d_matrix = {d_n: d for d_n, d in enumerate(d_matrix)}
    len_n = len(dict_d_matrix)
    taboo_cl = []
    result = []

    for i in range(len_n - 1):
        dict_d_matrix, taboo_cl, result = merge(dict_d_matrix, taboo_cl, result, len_n, method)
    return np.array(result)


Z = linkage(iris, "min")
# Z = [[101, 142, 0.0, 2], [7, 39, 0.09999999999999964, 2], [0, 17, 0.09999999999999998, 2], [9, 34, 0.1, 2], [128, 132, 0.10000000000000009, 2], [10, 48, 0.10000000000000053, 2], [40, 152, 0.14142135623730917, 3], [4, 37, 0.14142135623730925, 2], [19, 21, 0.14142135623730928, 2], [29, 30, 0.1414213562373093, 2], [57, 93, 0.1414213562373093, 2], [80, 81, 0.1414213562373093, 2], [116, 137, 0.1414213562373093, 2], [156, 157, 0.1414213562373093, 5], [8, 38, 0.14142135623730948, 2], [46, 158, 0.14142135623730953, 3], [1, 153, 0.14142135623730964, 3], [3, 47, 0.14142135623730964, 2], [27, 28, 0.14142135623730964, 2], [49, 151, 0.14142135623730964, 3], [82, 92, 0.14142135623730964, 2], [95, 96, 0.14142135623730964, 2], [127, 138, 0.14142135623730964, 2], [163, 169, 0.14142135623730964, 8], [2, 167, 0.14142135623730978, 3], [45, 166, 0.14142135623730986, 4], [12, 175, 0.1414213562373099, 5], [63, 91, 0.14142135623730995, 2], [65, 75, 0.14142135623730995, 2], [99, 171, 0.14142135623730995, 3], [159, 176, 0.14142135623730995, 7], [168, 173, 0.14142135623730995, 10], [25, 180, 0.17320508075688762, 8], [69, 161, 0.17320508075688762, 3], [123, 126, 0.17320508075688762, 2], [112, 139, 0.17320508075688787, 2], [174, 182, 0.17320508075688812, 11], [94, 179, 0.17320508075688815, 4], [88, 187, 0.1732050807568884, 5], [66, 84, 0.1999999999999993, 2], [78, 177, 0.19999999999999973, 3], [23, 26, 0.1999999999999998, 2], [42, 164, 0.20000000000000018, 3], [53, 89, 0.20000000000000018, 2], [74, 97, 0.20000000000000018, 2], [186, 192, 0.22360679774997827, 14], [11, 195, 0.22360679774997858, 15], [6, 196, 0.22360679774997871, 16], [35, 181, 0.22360679774997877, 11], [43, 191, 0.22360679774997896, 3], [70, 172, 0.22360679774997896, 3], [73, 190, 0.22360679774997896, 4], [155, 198, 0.22360679774997896, 13], [199, 202, 0.22360679774997902, 16], [197, 203, 0.22360679774997916, 32], [110, 147, 0.22360679774997935, 2], [120, 143, 0.22360679774997935, 2], [136, 148, 0.2449489742783171, 2], [58, 178, 0.24494897427831722, 3], [54, 208, 0.24494897427831766, 4], [67, 170, 0.24494897427831766, 3], [183, 193, 0.24494897427831766, 5], [146, 184, 0.24494897427831777, 3], [165, 204, 0.2449489742783178, 35], [103, 162, 0.24494897427831783, 3], [140, 144, 0.24494897427831785, 2], [13, 213, 0.244948974278318, 36], [141, 145, 0.24494897427831822, 2], [200, 212, 0.24494897427831838, 6], [68, 87, 0.26457513110645864, 2], [188, 210, 0.26457513110645864, 8], [194, 209, 0.2645751311064587, 6], [113, 150, 0.26457513110645897, 2], [50, 52, 0.26457513110645914, 2], [90, 220, 0.26457513110645914, 9], [211, 224, 0.2645751311064592, 14], [51, 56, 0.2645751311064593, 2], [107, 130, 0.26457513110645936, 2], [206, 215, 0.26457513110645947, 4], [105, 122, 0.26457513110645964, 2], [149, 218, 0.282842712474618, 7], [20, 31, 0.282842712474619, 2], [86, 223, 0.2828427124746193, 3], [24, 216, 0.2999999999999998, 37], [124, 228, 0.2999999999999998, 5], [36, 233, 0.3, 38], [61, 225, 0.3000000000000001, 15], [115, 207, 0.3000000000000001, 3], [231, 235, 0.3000000000000001, 40], [104, 154, 0.30000000000000016, 3], [55, 189, 0.30000000000000027, 3], [121, 222, 0.31622776601683755, 3], [221, 226, 0.31622776601683755, 8], [236, 240, 0.3162277660168378, 18], [232, 242, 0.31622776601683783, 11], [77, 244, 0.31622776601683794, 12], [76, 245, 0.31622776601683816, 13], [83, 133, 0.33166247903553975, 2], [201, 243, 0.33166247903553975, 22], [5, 18, 0.33166247903553986, 2], [230, 241, 0.33166247903553997, 10], [71, 246, 0.33166247903554, 14], [214, 239, 0.3316624790355402, 6], [111, 205, 0.34641016151377513, 3], [185, 234, 0.34641016151377513, 7], [16, 238, 0.3464101615137753, 41], [248, 251, 0.3464101615137753, 36], [249, 255, 0.3464101615137753, 43], [32, 33, 0.3464101615137755, 2], [257, 258, 0.3464101615137755, 45], [125, 129, 0.3464101615137756, 2], [79, 256, 0.3464101615137758, 37], [72, 247, 0.3605551275463984, 3], [44, 259, 0.3605551275463988, 46], [252, 253, 0.3605551275463988, 9], [60, 160, 0.3605551275463989, 3], [217, 264, 0.3605551275463989, 11], [250, 262, 0.3605551275463989, 13], [254, 266, 0.360555127546399, 18], [15, 263, 0.3605551275463992, 47], [237, 268, 0.374165738677394, 21], [85, 261, 0.3741657386773941, 38], [267, 270, 0.3741657386773942, 34], [98, 265, 0.3872983346207412, 4], [59, 271, 0.38729833462074165, 39], [102, 260, 0.38729833462074187, 3], [272, 275, 0.3999999999999997, 37], [118, 229, 0.4123105625617659, 3], [14, 269, 0.412310562561766, 48], [117, 131, 0.4123105625617661, 2], [274, 276, 0.41231056256176624, 76], [64, 280, 0.4242640687119284, 77], [100, 281, 0.42426406871192884, 78], [119, 282, 0.43588989435406705, 79], [227, 283, 0.43588989435406733, 81], [22, 278, 0.45825756949558394, 49], [114, 284, 0.4898979485566353, 82], [62, 286, 0.4898979485566356, 83], [219, 287, 0.5099019513592786, 85], [277, 288, 0.5291502622129179, 88], [135, 289, 0.5385164807134504, 89], [134, 290, 0.5385164807134505, 90], [108, 291, 0.5567764362830021, 91], [41, 285, 0.6244997998398398, 50], [109, 292, 0.6324555320336759, 92], [273, 294, 0.6480740698407862, 96], [106, 295, 0.7348469228349535, 97], [279, 296, 0.818535277187245, 99], [293, 297, 1.6401219466856727, 149]]

print(list(Z))


def cluster_dist(Z, T, cutoff, n):
    max_dists = np.ndarray(n, dtype=np.double)
    get_max_dist_for_each_cluster(Z, max_dists, n)
    cluster_monocrit(Z, max_dists, T, cutoff, n)


def get_labels(Z, t):
    # Z = np.asarray(Z, order='c')
    n = Z.shape[0] + 1
    T = np.zeros((n,), dtype='i')
    cluster_dist(Z, T, t, int(n))
    return T


def is_visited(visited, x):
    return x in visited


def set_visited(visited, x):
    visited.append(x)


def get_max_dist_for_each_cluster(Z: np.ndarray, MD, n):
    curr_node = np.ndarray(n, dtype=np.intc)

    visited = []

    k = 0
    curr_node[0] = 2 * n - 2
    while k >= 0:
        root = curr_node[k] - n
        i_lc = int(Z[root, 0])
        i_rc = int(Z[root, 1])

        if i_lc >= n and not is_visited(visited, i_lc):
            set_visited(visited, i_lc)
            k += 1
            curr_node[k] = i_lc
            continue

        if i_rc >= n and not is_visited(visited, i_rc):
            set_visited(visited, i_rc)
            k += 1
            curr_node[k] = i_rc
            continue

        max_dist = Z[root, 2]
        if i_lc >= n:
            # print(i_lc, n, i_lc-n)
            max_l = MD[i_lc - n]
            if max_l > max_dist:
                max_dist = max_l
        if i_rc >= n:
            max_r = MD[i_rc - n]
            if max_r > max_dist:
                max_dist = max_r
        MD[root] = max_dist

        k -= 1

    del visited


def cluster_monocrit(Z, MC, T, cutoff, n):
    n_cluster = 0
    cluster_leader = -1
    curr_node = np.ndarray(n, dtype=np.intc)

    visited = []

    k = 0
    curr_node[0] = 2 * n - 2
    while k >= 0:
        root = curr_node[k] - n
        i_lc = int(Z[root, 0])
        i_rc = int(Z[root, 1])

        if cluster_leader == -1 and MC[root] <= cutoff:  # found a cluster
            cluster_leader = root
            n_cluster += 1

        if i_lc >= n and not is_visited(visited, i_lc):
            set_visited(visited, i_lc)
            k += 1
            curr_node[k] = i_lc
            continue

        if i_rc >= n and not is_visited(visited, i_rc):
            set_visited(visited, i_rc)
            k += 1
            curr_node[k] = i_rc
            continue

        if i_lc < n:
            if cluster_leader == -1:  # singleton cluster
                n_cluster += 1
            T[i_lc] = n_cluster

        if i_rc < n:
            if cluster_leader == -1:  # singleton cluster
                n_cluster += 1
            T[i_rc] = n_cluster

        if cluster_leader == root:  # back to the leader
            cluster_leader = -1
        k -= 1

    del visited


# my_labels = fcluster(Z, t=0.9, criterion='distance')
# print(my_labels)


plt.figure(figsize=(15, 10))
_ = dendrogram(Z, p=20, truncate_mode="lastp")
plt.show()
#
my_labels = get_labels(Z1, t=3)
not_my_labels = fcluster(Z, t=3, criterion='distance')
# print(Z1 == Z)
# print(not_my_labels)
print(all(not_my_labels == my_labels))
# plt.figure(figsize=(15, 10))
_ = dendrogram(Z1, p=20, truncate_mode="lastp")
plt.show()
pdist()
# array([[7., 9., 0.3, 2.],
#        [4., 6., 0.5, 2.],
#        [5., 12., 0.5, 3.],
#        [2., 13., 0.53851648, 4.],
#        [3., 14., 0.58309519, 5.],
#        [1., 15., 0.64031242, 6.],
#        [10., 11., 0.72801099, 3.],
#        [8., 17., 1.2083046, 4.],
#        [0., 16., 1.5132746, 7.],
#        [18., 19., 1.92353841, 11.]])
from sklearn.cluster import KMeans

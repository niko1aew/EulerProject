# Пути через таблицу

# Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться только вниз или вправо,
# существует ровно 6 маршрутов до правого нижнего угла сетки.

# Сколько существует таких маршрутов в сетке 20×20?
import networkx as nx
import matplotlib.pyplot as plt
import Utils
import math


def count_paths(w, h):
    G = nx.DiGraph()

    # Вычисляем необходимое количество узлов
    nodes_count = (w + 1) * (h + 1)

    # Добавляем узлы в граф
    for i in range(1, nodes_count + 1, 1):
        G.add_node(i)
    for i in range(1, nodes_count + 1):
        if not i % (w + 1) == 0:
            G.add_edge(i, i + 1)
        if i <= nodes_count-(w+1):
            G.add_edge(i, i+h+1)

    paths = nx.all_shortest_paths(G, source=1, target=nodes_count)
    nx.draw(G, with_labels=True)
    plt.show()
    return len(list(paths))


def task_15_graph_solution():
    print(count_paths(12, 12))


def task_15_binary_bits_solution():
    size = 20
    p = math.factorial(size*2)/(math.factorial(size)**2)
    print("В сетке "+str(size)+"х"+str(size) + " "+str(int(p))+" маршрутов")


Utils.run_task(task_15_binary_bits_solution)

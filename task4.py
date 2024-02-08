import uuid

import networkx as nx
import matplotlib.pyplot as plt
import heapq

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def build_heap_tree(heap_array):
    heap_root = None

    def build_heap(node, idx):
        nonlocal heap_root
        if idx < len(heap_array):
            node = Node(heap_array[idx])
            heap_root = node
            node.left = build_heap(node.left, 2 * idx + 1)
            node.right = build_heap(node.right, 2 * idx + 2)
        return node

    heap_root = build_heap(heap_root, 0)
    return heap_root

# Бінарна купа у вигляді масиву
heap_array = [0, 4, 10, 5, 3, 1]
heapq.heapify(heap_array)

# Побудова дерева з купи
heap_tree_root = build_heap_tree(heap_array)

# Відображення бінарної купи з дерева
draw_tree(heap_tree_root)

import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

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

def draw_tree(tree_root, traversal_path):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    node_colors = {}
    for i, (node_val, _) in enumerate(traversal_path):
        color_intensity = 240 - i * 15 
        color = "#{:02x}{:02x}{:02x}".format(0x12, 0x96, color_intensity)
        node_colors[node_val] = color

    colors = [node_colors[node[1]['label']] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def dfs(node):
    if node is None:
        return []
    stack = [(node, '#1296F0')]
    path = []
    while stack:
        curr_node, curr_color = stack.pop()
        path.append((curr_node.val, curr_color))
        if curr_node.right:
            stack.append((curr_node.right, lighter_color(curr_color)))
        if curr_node.left:
            stack.append((curr_node.left, lighter_color(curr_color)))
    return path

def bfs(node):
    if node is None:
        return []
    queue = deque([(node, '#1296F0')])
    path = []
    while queue:
        curr_node, curr_color = queue.popleft()
        path.append((curr_node.val, curr_color))
        if curr_node.left:
            queue.append((curr_node.left, lighter_color(curr_color)))
        if curr_node.right:
            queue.append((curr_node.right, lighter_color(curr_color)))
    return path

def lighter_color(color):
    # Функція, яка змінює колір на світліший
    r = min(int(color[1:3], 16) + 40, 255)
    g = min(int(color[3:5], 16) + 40, 255)
    b = min(int(color[5:], 16) + 40, 255)
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

def print_path(traversal_type, path):
    print(f"{traversal_type} Paths: {[node[0] for node in path]}")


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Обхід дерева в глибину
dfs_path = dfs(root)
print_path("DFS", dfs_path)
draw_tree(root, dfs_path)

# Обхід дерева в ширину
bfs_path = bfs(root)
print_path("BFS", bfs_path)
draw_tree(root, bfs_path)

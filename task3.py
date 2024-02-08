import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Створення напрямленого графа
G = nx.DiGraph()

# Додавання вершин
G.add_node("A", pos=(0, 0))
G.add_node("B", pos=(1, 0))
G.add_node("C", pos=(2, 0))
G.add_node("D", pos=(1, 1))
G.add_node("E", pos=(1, -1))

# Додавання ребер з вагами (наприклад, часом подорожі)
G.add_edge("A", "B", weight=5)
G.add_edge("B", "C", weight=3)
G.add_edge("B", "D", weight=2)
G.add_edge("B", "E", weight=4)

def dijkstra(graph, start):
    # Ініціалізація
    distances = {node: float('inf') for node in graph.nodes()}
    distances[start] = 0
    pq = [(0, start)]  # Початковий елемент черги пріоритетів
    
    # Основний цикл алгоритму Дейкстри
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # Якщо знайдено більш короткий шлях, оновити відстань
        if current_distance > distances[current_node]:
            continue
        
        # Прохід по сусідах поточного вузла
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight['weight']
            
            # Оновлення відстаней, якщо новий шлях коротший
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Виклик функції та вивід результатів
start_node = "A"
shortest_distances = dijkstra(G, start_node)
print(f"Найкоротші відстані від вершини {start_node}: {shortest_distances}")

# Візуалізація графа
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=12, font_weight="bold", arrowsize=20)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()
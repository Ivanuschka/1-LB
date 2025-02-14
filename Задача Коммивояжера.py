import itertools
import networkx as nx
import matplotlib.pyplot as plt

# Создаем граф
G = nx.Graph()

# Города
towns = ["Город A", "Город B", "Город C", "Город D", "Город E",
         "Город F", "Город G", "Город H", "Город I", "Город J"]

G.add_nodes_from(towns)

# Ребра с расстояниями
roads = [("Город A", "Город B", 15), ("Город A", "Город C", 10), 
         ("Город B", "Город D", 12), ("Город C", "Город D", 8),
         ("Город C", "Город E", 20), ("Город D", "Город E", 5),
         ("Город E", "Город F", 18), ("Город F", "Город G", 7),
         ("Город G", "Город H", 10), ("Город H", "Город I", 6),
         ("Город I", "Город J", 8), ("Город J", "Город A", 14),
         ("Город D", "Город G", 22), ("Город B", "Город H", 25)]

# Добавляем рёбра
for town1, town2, distance in roads:
    G.add_edge(town1, town2, weight=distance)

# Перебираем все возможные маршруты через 3 промежуточных города
start = "Город E"
end = "Город I"
all_towns = set(G.nodes) - {start, end}
best_path = None
min_distance = float("inf")

for mid_points in itertools.permutations(all_towns, 3):  # Три промежуточных города
    route = [start] + list(mid_points) + [end]
    
    # Проверяем, есть ли все рёбра в маршруте
    if all(G.has_edge(route[i], route[i+1]) for i in range(len(route)-1)):
        total_distance = sum(G[route[i]][route[i+1]]['weight'] for i in range(len(route)-1))

        if total_distance < min_distance:
            min_distance = total_distance
            best_path = route

# Визуализация графа
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)  # Расположение узлов

# Отображаем весь граф
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', 
        node_size=2000, font_size=10, font_weight='bold')

# Подписываем рёбра (расстояния)
edge_labels = {(town1, town2): f"{distance} км" for town1, town2, distance in roads}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

# Проверяем, найден ли маршрут
if best_path:
    best_edges = [(best_path[i], best_path[i+1]) for i in range(len(best_path)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=best_edges, edge_color='red', width=2.5)
    print(f"Кратчайший маршрут: {' → '.join(best_path)} (Длина: {min_distance} км)")
else:
    print("Маршрут не найден!")

plt.title("Минимальный маршрут")
plt.show()

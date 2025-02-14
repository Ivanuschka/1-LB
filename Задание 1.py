import networkx as nx
import matplotlib.pyplot as plt

# Создаем граф
G = nx.Graph()

# Список населенных пунктов
towns = ["Город A", "Город B", "Город C", "Город D", "Город E",
         "Город F", "Город G", "Город H", "Город I", "Город J"]

G.add_nodes_from(towns)

# Список дорог с расстояниями (весами рёбер)
roads = [("Город A", "Город B", 15), ("Город A", "Город C", 10), 
         ("Город B", "Город D", 12), ("Город C", "Город D", 8),
         ("Город C", "Город E", 20), ("Город D", "Город E", 5),
         ("Город E", "Город F", 18), ("Город F", "Город G", 7),
         ("Город G", "Город H", 10), ("Город H", "Город I", 6),
         ("Город I", "Город J", 8), ("Город J", "Город A", 14),
         ("Город D", "Город G", 22), ("Город B", "Город H", 25)]

# Добавляем рёбра с расстояниями
for town1, town2, distance in roads:
    G.add_edge(town1, town2, weight=distance)

# Оптимальный путь (выделенный маршрут)
shortest_path = [("Город E", "Город D"), ("Город D", "Город G"),
                 ("Город G", "Город H"), ("Город H", "Город I")]

# Визуализация графа
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)  # Расположение узлов

# Рисуем узлы и рёбра
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', 
        node_size=2000, font_size=10, font_weight='bold')

# Подписываем рёбра (расстояния)
edge_labels = {(town1, town2): f"{distance} км" for town1, town2, distance in roads}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

# Выделяем кратчайший путь красным цветом
nx.draw_networkx_edges(G, pos, edgelist=shortest_path, edge_color='red', width=2.5)

plt.title("Минимальный маршрут между Городом E и Городом I")
plt.show()

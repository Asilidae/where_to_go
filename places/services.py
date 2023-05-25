import math
from math import inf, sqrt
from itertools import permutations
import folium
import openrouteservice
from openrouteservice.directions import directions

# Функция для вычисления евклидова расстояния между двумя точками
def distance(point1, point2):
    return sqrt((point1['lon'] - point2['lon'])**2 + (point1['lng'] - point2['lng'])**2)

# Функция для вычисления общего расстояния по маршруту
def total_distance(route):
    return sum(distance(route[i], route[i - 1]) for i in range(len(route)))

# Функция для нахождения оптимального маршрута
def optimal_route(points):
    min_distance = inf
    min_route = None
    for route in permutations(points):
        route_distance = total_distance(route)
        if route_distance < min_distance:
            min_distance = route_distance
            min_route = route
    return min_route, min_distance

def map_generated(min_route):
    # Создаем карту, центрированную на первой точке маршрута
    m = folium.Map(location=[min_route[0]['lon'], min_route[0]['lng']], zoom_start=6)

    # Добавляем маркеры для каждой точки
    for point in min_route:
        folium.Marker([point['lon'], point['lng']], popup=point['place_id']).add_to(m)

    # Добавляем линии между точками
    folium.PolyLine([(point['lon'], point['lng']) for point in min_route], color="red", weight=2.5, opacity=1).add_to(m)

    # Отображаем карту
    m.save('map.html')



# Функция для вычисления расстояния между двумя точками
def calculate_distance(point1, point2):
    lon1, lat1 = point1['lon'], point1['lng']
    lon2, lat2 = point2['lon'], point2['lng']
    return math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)

# Метод ближайшего соседа
def nearest_neighbour(data):
    current_point = data[0]
    route = [current_point]
    unvisited_points = data[1:]

    while unvisited_points:
        next_point = min(unvisited_points, key=lambda point: calculate_distance(current_point, point))
        unvisited_points.remove(next_point)
        route.append(next_point)
        current_point = next_point

    return route




# points = [
#     {'id': '1', 'lat': 50.45, 'lng': 30.52},
#     {'id': '2', 'lat': 52.52, 'lng': 13.40},
#     {'id': '3', 'lat': 48.85, 'lng': 2.35},
#     {'id': '4', 'lat': 51.51, 'lng': -0.13}
# ]

# min_route, min_distance = optimal_route(points)
# print(min_route)
# for point in min_route:
#     print(point['id'])
#
# print("Total distance:", min_distance)
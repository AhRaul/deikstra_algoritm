"""
Визуальное представление рассматриваемых путей. 

из начала в "A" (расстояние 6);
из "A" в конец  (расстояние 1);
из начала в "B" (расстояние 2);
из "B" в конец  (расстояние 5);
из "B" в "A"    (расстояние 3).

(в PyCharm у меня этот комментарий ровно отображается, 
в другом редакторе или браузере, может съехать.)
__________________________
         "A"
 6     ^  ^  \     1
      /   |   \/
начало   3|   конец
      \   |   ^
 2     \/ |  /     5
         "B"
__________________________
"""

graph = {}      #Таблица связей и стоимостей, основная, неизменная таблица

#от начальной точки всего 2 пути. Через точку A и через точку B
graph["начало"] = {}
graph["начало"]["a"] = 6
graph["начало"]["b"] = 2

#из точки A всего один путь, к конечной.
graph["a"] = {}
graph["a"]["конец"] = 1

#Из точки B два пути. Через точку A, и к конечной точке.
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["конец"] = 5

#Конечная точка не имеет путей.
graph["конец"] = {}

infinity = float("inf")                 #Инициализируем бесконечность
costs = {}                              #Минимальные стоимости, от начала, до вычисленной точки.
                                            # Переменные нужны, для обновления минимальной стоимости пути,
                                            # если более короткий путь будет найден.
costs["a"] = 6                          #От начала до точки а
costs["b"] = 2                          #от начала до точки b
costs["конец"] = infinity               #от начала до конца пока неизвестно, поэтому,
                                            # расстояние считается бесконечным,
                                            # согласно алгоритму Дейкстры.

parents = {}                            #Родительские узлы. Если будет найден более короткий путь к точке,
                                            # то родитель будет заменён на того, через кого короткий путь пролегает.
parents["a"] = "начало"
parents["b"] = "начало"
parents["конец"] = None

processed = []          # Список уже обработанных узлов.

def find_lowest_cost_node(costs):
    """
    Метод поиска наименьшей стоимости пути от начальной до связанных с начальной, точек
    :param costs: список известных стоимостей (в случае, если минимальный путь до точки не найден,
    то приведен заданный прямой путь до точки)
    :return: возвращает точку с минимальной ценой он начальной точки (например "начало" - точка "B")
    """
    lowest_cost = float("inf")  #Кратчайший путь неизвестен, потому равен бесконечности.
                                    # (бесконечность нужна для корректного сравнения большего с меньшим)
    lowest_cost_node = None     #Точка, с кратчайшим путем от начальной.
    for node in costs:          #перебор всех имеющихся узлов
        cost = costs[node]      #Стоимость узла
        if cost < lowest_cost and node not in processed:    #закидываем стоимость первого узла в переменную
                                                                # наименьшего, и далее сравниваем его с новым узлом.
            lowest_cost = cost              #Минимальная цена
            lowest_cost_node = node         #Точка с минимальной ценой
    return lowest_cost_node

"""
Алгоритм Дейкстры в действии.
"""
node = find_lowest_cost_node(costs)     # Найти узел с наименьшей стоймостью среди необработанных
while node is not None:                 # Если обработаны все узлы, цикл while завершён
    cost = costs[node]                  # Наименьшая стоимость узла
    neighbors = graph[node]             # Внешние соседи
    for n in neighbors.keys():          # Перебрать всех соседей (neighbors) текущего узла
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:         # Если к соседу можно быстрее добраться через текущий узел
            costs[n] = new_cost         # Обновить стоимость этого узла
            parents[n] = node           # Этот узел становится новым родителем для соседа
    processed.append(node)              # Узел помечается как обработанный
    node = find_lowest_cost_node(costs) # Найти следующий узел для обработки и повторить цикл

print("кротчайший путь от начальной до конечной точки, будет равен: " + str(costs["конец"]))
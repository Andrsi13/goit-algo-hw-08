import heapq


def min_cost_to_connect_cables(cable_lengths):
    # Ініціалізація мін-купи
    heapq.heapify(cable_lengths)
    
    total_cost = 0
    
    # Поки в купі більше одного елемента
    while len(cable_lengths) > 1:
        # Витягуємо два найменші елементи
        first_min = heapq.heappop(cable_lengths)
        print(f'перший елемент: {first_min}')
        second_min = heapq.heappop(cable_lengths)
        print(f'перший елемент: {second_min}')
        
        # Витрати на з'єднання двох кабелів
        cost = first_min + second_min
        print(cost)
        
        # Додаємо витрати до загальних витрат
        total_cost += cost
        
        # Додаємо об'єднаний кабель назад до купи
        heapq.heappush(cable_lengths, cost)
    
    return total_cost

# Приклад використання
cable_lengths = [4, 3, 2, 6]
print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cable_lengths))

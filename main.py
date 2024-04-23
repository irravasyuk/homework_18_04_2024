# Завдання 1
# Розробіть додаток, що імітує чергу запитів до сервера.
# Мають бути клієнти, які надсилають запити на сервер, кожен
# з яких має свій пріоритет. Кожен новий клієнт потрапляє у
# чергу залежно від свого пріоритету. Зберігайте статистику
# запитів (користувач, час) в окремій черзі.
# Передбачте виведення статистики на екран. Вибір необхідних
# структур даних визначте самостійно.
# from queue import PriorityQueue
# import time
# import random
#
# class RequestsServer:
#     def __init__(self):
#         self.queue = PriorityQueue()
#         self.request_stats = []
#
#     def add_client(self, client, priority):
#         self.queue.put((priority, client))
#
#     def request_processing(self):
#         if self.queue.empty():
#             print('Всі запити оброблені.')
#             return
#
#         priority, request = self.queue.get()
#
#         processing_time = random.randint(1, 5)
#         time.sleep(processing_time)
#
#         self.request_stats.append((request, time.time()))
#
#         print(f'Виконую {request} (час обробки: {processing_time} сек.)')
#
#     def display_stat(self):
#         print('Статистика запитів:')
#         for i, (request, timestamp) in enumerate(self.request_stats, start=1):
#             print(f"{i}. {request} = {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))}")
#
# processing = RequestsServer()
#
# processing.add_client('Запит 2', 2)
# processing.add_client('Запит 3', 3)
# processing.add_client('Запит 1', 1)
#
# processing.request_processing()
# processing.request_processing()
# processing.request_processing()
#
# processing.display_stat()


# Завдання 2
# Створіть імітаційну модель «Причал морських катерів».
# Введіть таку інформацію:
# 1. Середній час між появою пасажирів на причалі у різний
# час доби;
# 2. Середній час між появою катерів на причалі у різний час
# доби;
# 3. Тип зупинки катера (кінцева або інша).
# Визначіть:
# 1. Середній час перебування людини на зупинці;
# 2. Достатній інтервал часу між приходами катерів, коли на
# зупинці не більше N людей одночасно;
# 3. Кількість вільних місць у катері є випадковою величиною.
# Вибір необхідних структур даних визначте самостійно.
import random
import time
from queue import Queue

class Passenger:
    def __init__(self, id):
        self.id = id

class Boat:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def boarding_passengers(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            return True
        else:
            return False

class Berth:
    def __init__(self, average_boat_time, average_passenger_time, max_passengers):
        self.passenger_queue = Queue()
        self.boat_queue = Queue()
        self.average_boat_time = average_boat_time
        self.average_passenger_time = average_passenger_time
        self.max_passengers = max_passengers

    def add_passenger(self, passenger):
        self.passenger_queue.put(passenger)

    def simulate(self, simulate_time):
        start_time = time.time()
        while time.time() - start_time < simulate_time:
            if random.random() < 1.0 / self.average_boat_time:
                boat = Boat(5)
                self.boat_queue.put(boat)
                print('Катер прибув.')

            if random.random() < 1.0 / self.average_passenger_time:
                passenger = Passenger(len(self.passenger_queue.queue) + 1)
                self.add_passenger(passenger)
                print('Пасажир прибув на причал.')

            if not self.boat_queue.empty() and not self.passenger_queue.empty():
                boat = self.boat_queue.queue[0]
                passenger = self.passenger_queue.get()
                if boat.boarding_passengers(passenger):
                    print(f"Пасажир {passenger.id} сів на катер")
                else:
                    print(f"Катер повний. Пасажиру {passenger.id} немає куди сісти")

            time.sleep(1)

average_boat_time = 30
average_passenger_time = 10
max_passengers = 20
simulate_time = 300

berth = Berth(average_boat_time, average_passenger_time, max_passengers)

berth.simulate(simulate_time)








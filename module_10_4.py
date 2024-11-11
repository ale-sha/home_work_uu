import random
from queue import Queue
from threading import Thread, Lock
from time import sleep


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(random.randint(3,10))
        print(f'{self.name} поел и ушёл')

class Cafe:
    def __init__(self, *args):
        self.queue = Queue()
        self.tables = args
        self.lock = Lock()

    def guest_arrival(self, *guests: Guest):
        for guest in guests:
            with self.lock:
                busy = False
                for table in self.tables:
                    if table.guest is None:
                        table.guest = guest
                        guest.start()
                        print(f'{guest.name} сел(-а) за стол номер {table.number}')
                        busy = True
                        break
                if not busy:
                    self.queue.put(guest)
                    print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while True:
            with self.lock:
                for table in self.tables:
                    if table.guest is not None and not table.guest.is_alive():
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None
                    elif not self.queue.empty() and table.guest is None:
                        guest_queue = self.queue.get()
                        table.guest = guest_queue
                        table.guest.start()
                        print(f"{guest_queue.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                    sleep(1)


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

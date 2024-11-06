import threading
from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        count_day = 0
        adversary = 100
        print(f'"{self.name}, на нас напали!"')
        while adversary > 0:
            count_day += 1
            adversary -= self.power
            print(f'"{self.name} сражается {count_day} дней, осталось {adversary} воинов."')
            time.sleep(1)
        print(f'"{self.name} одержал победу спустя {count_day} дней(дня)!"')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')

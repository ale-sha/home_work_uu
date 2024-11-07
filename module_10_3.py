import threading
from threading import Thread
import random
import time

class Bank:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            income = random.randint(50,500)
            self.lock.acquire()
            if self.balance >= 500:
                self.lock.release()
            else:
                self.balance += income
                print(f'Пополнение: {income}. Баланс: {self.balance}.')
            if self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            expense = random.randint(50,500)
            print(f"Запрос на снятие {expense}")
            self.lock.acquire()
            if expense <= self.balance:
                self.balance -= expense
                print(f"Снятие: {expense}. Баланс: {self.balance}.")
            else:
                print("Запрос отклонён, недостаточно средств")
            if self.lock.locked():
                self.lock.release()
            time.sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

import threading
import time
import random
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

    def set_guest(self, guest):
        self.guest = guest

    @property
    def is_occupied(self):
        return self.guest is not None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time_to_wait = random.randint(3, 10)
        print(f'{self.name} будет ждать {time_to_wait} секунд')
        time.sleep(time_to_wait)


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            if any(table.is_occupied for table in self.tables):
                free_table = next((table for table in self.tables if not table.is_occupied), None)
                if free_table:
                    free_table.set_guest(guest)
                    guest.start()
                    guest.join()
                    print(f'{guest.name} сел(-а) за стол номер {free_table.number}')
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty():
            guest = self.queue.get()
            free_table = next((table for table in self.tables if not table.is_occupied), None)
            if free_table:
                free_table.set_guest(guest)
                guest.start()
                guest.join()
                print(f'{guest.name} сел(-а) за стол номер {free_table.number}')


tables = [Table(number) for number in range(1, 6)]

guest_names = [
    'Anastasia', 'Andrey', 'Sergey', 'Nadya', 'Pavel', 'Valentina',
    'Dmytro', 'Yana', 'Maria', 'Anton', 'Alexandr', 'German'
]

guests = [Guest(name) for name in guest_names]

cafe = Cafe(*tables)

cafe.guest_arrival(*guests)

cafe.discuss_guests()

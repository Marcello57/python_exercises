import threading
import time
import random


class Philosopher(threading.Thread):
    def __init__(self, name, left, right):
        threading.Thread.__init__(self)
        self.name = name
        self.left_fork = left
        self.right_fork = right

    def run(self):
        time.sleep(random.random() + 0.2)
        print('Philosopher {} is hungry.'.format(self.name))
        self.dine()

    def dine(self):

        while True:
            locked1 = self.left_fork.acquire(False)
            locked2 = self.right_fork.acquire(False)
            if locked2 and locked1:
                break
            time.sleep(random.random() + 0.1)

        print('Philosopher {} starts eating.'.format(self.name))
        time.sleep(random.random() + 0.1)
        print('Philosopher {} finishes eating.'.format(self.name))
        self.left_fork.release()
        self.right_fork.release()


if __name__ == "__main__":
    forks = [threading.Lock() for n in range(5)]

    philosophers = [Philosopher(i, forks[i], forks[(i + 1) % 5]) for i in range(5)]

    for p in philosophers:
        p.start()

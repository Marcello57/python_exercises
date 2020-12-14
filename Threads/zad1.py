import threading
import random

data = [random.randint(1, 10000) for i in range(0, 20000)]

histogram = [0, 0, 0, 0, 0]


def count_data(range_start, range_end):
    for pos in range(range_start, range_end):
        histogram[int((data[pos]-1)/2000)] += 1


thread1 = threading.Thread(target=count_data(0, 3999))
thread2 = threading.Thread(target=count_data(4000, 7999))
thread3 = threading.Thread(target=count_data(8000, 11999))
thread4 = threading.Thread(target=count_data(12000, 15999))
thread5 = threading.Thread(target=count_data(16000, 19999))

print(histogram)

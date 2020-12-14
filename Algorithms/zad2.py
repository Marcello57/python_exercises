from random import randint

numbers = []
for pos in range(0, 50):
    numbers.append(randint(0, 1000))


def bubble_sort(my_list):
    # We go through the list as many times as there are elements
    for i in range(len(my_list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(my_list) - i - 1):
            if my_list[j] > my_list[j+1]:
                # Swap
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    my_list.reverse()
    return my_list

print(bubble_sort(numbers))
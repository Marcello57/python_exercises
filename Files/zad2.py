import os

print('Enter directory path:')
base_dir = input()


def file_search(b_dir):
    for name in os.listdir(b_dir):
        new_dir = '\\{}'.format(name)
        new_dir = b_dir + new_dir
        if os.path.isfile(new_dir):
            print(name)
        elif os.path.isdir(new_dir):
            file_search(new_dir)


if __name__ == "__main__":
    file_search(base_dir)

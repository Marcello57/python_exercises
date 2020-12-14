file_list = ['Albanian cuisine.txt', 'Art film.txt', 'Assyrian captivity.txt', 'Australian House of Representatives.txt', 'Austrian Armed Forces.txt', 'Axolemma.txt', 'Bahrain.txt']

for files in file_list:
    with open(files, "r") as file:
        my_string_list = file.readlines()

    out_string = ""
    for line in my_string_list:
        # i cant find polish files in repository, so I'm deleting english words
        line = line.replace("myself", "")
        line = line.replace("and", "")
        line = line.replace("why", "")
        line = line.replace("never", "")
        out_string += line
    #print(out_string)

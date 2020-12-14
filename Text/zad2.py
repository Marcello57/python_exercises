file_list = ['Albanian cuisine.txt', 'Art film.txt', 'Assyrian captivity.txt', 'Australian House of Representatives.txt', 'Austrian Armed Forces.txt', 'Axolemma.txt', 'Bahrain.txt']

# i cant find polish files in repository, so I'm replacing english words
dict = {
    "and"  : "or",
    "or"   : "and",
    "never": "hardly ever",
    "why"  : "forwhy"
}

for files in file_list:
    with open(files, "r") as file:
        my_string_list = file.readlines()

    out_string = ""  # it's only for checking if it's working, not for storing files
    for line in my_string_list:
        for key in dict.keys():
            line.replace(key, dict[key])
        out_string += line
    # print(out_string)

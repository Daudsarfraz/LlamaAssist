import os
def create_file(file_name):
    search_file = os.listdir(file_name)
    print(search_file)



create_file("words_count.txt")


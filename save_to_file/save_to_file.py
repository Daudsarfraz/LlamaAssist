import os

# def read_file(file_name, mode = None):
#     with open(file_name, mode) as f:
#         print(f.read())
#     f.close()


def create_file(file_name, content, moode = "a"):

    try:
        file_found = [i for i in os.listdir(os.getcwd()) if i==file_name]
        if file_found:
            with open(file_name, moode) as f:
                f.write(content)
            f.close()
        else:
            with open(file_name, moode) as f:
                f.write(content)
            f.close()
    except Exception as e:
            print(f"{e}")




content = "I am LLAMA 3"
file_name = "words_count12.txt"
create_file(file_name, content)
# read_file(file_name, mode="r")



import os
def create_file(file_name):

    try:
        file_found = [i for i in os.listdir(os.getcwd()) if i==file_name]
        if file_found:
            print("Entered File Found", file_name)
        else:
             with open(file_name, "w") as f:
                  print(f"File {file_name} has been created")



    except Exception as e:
            print(f"{e}")
        # with open(file_name, "a") as f:
        #     print("File is Created", file_name)

        #     f.close()





file_name = "words_count12.txt"
create_file(file_name)


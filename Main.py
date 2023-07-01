import os

def remove_file_extension():
    current_path = os.getcwd()
    file_list = os.listdir(current_path)

    for file_name in file_list:
        file_path = os.path.join(current_path, file_name)
        if os.path.isfile(file_path):
            file_name_without_extension, _ = os.path.splitext(file_name) 
            new_file_path = os.path.join(current_path, file_name_without_extension)
            os.rename(file_path, new_file_path)

if __name__ == '__main__':
    remove_file_extension()

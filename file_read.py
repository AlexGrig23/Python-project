import os
if __name__ == "__main__":

    filename = "example.txt"
def read():
    abs_path = os.path.abspath(__file__)
    base_dir = os.path.dirname(abs_path)
    file_path = os.path.join(base_dir, "files", filename)
    try:
        file_read = open(file_path, "r", encoding='UTF-8')
        file_read.seek(0)
        return file_read.read()
    except FileNotFoundError:
        return "This file does not exist, please confirm the name or address"
    finally:
        print("Program complited")

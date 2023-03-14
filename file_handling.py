import os
if __name__ == "__main__":

    filename = "example.txt"


def reading_file():
    ab_path = os.path.abspath(__file__)
    base_dir = os.path.dirname(ab_path)
    file_path = os.path.join(base_dir, "files", filename)
    fil_read = open(file_path, "r", encoding='UTF-8')
    try:
        fil_read.seek(0)
        return fil_read.read()
    except FileNotFoundError:
        return "This file does not exist, please confirm the name or address"
    finally:
        fil_read.close()
        print("Program complited")


def access():
    f = "example.txt"
    abs_path = os.path.abspath(__file__)
    based_dir = os.path.dirname(abs_path)
    f_path = os.path.join(based_dir, "files", f)
    os.chmod(f_path, 0o444)
    f_r = open(f_path, "r", encoding='UTF-8')
    try:
        f_r = open(f_path, "w", encoding='UTF-8')
        f_r.write(f"Word Hello in text times")
        return f_r.read()
    except PermissionError:
        return "You do not have access to this file, contact your administrator"
    finally:
        f_r.close()
        print("Program complited")


def exam_int():
    ab_path = os.path.abspath(__file__)
    base_dir = os.path.dirname(ab_path)
    file_path = os.path.join(base_dir, "files", filename)
    f_read = open(file_path, "r", encoding='UTF-8')
    try:
        for i in f_read:
            print(int(i))
    except ValueError:
        return "The file contains not only numerical values"
    finally:
        f_read.close()
        print("Program complited")

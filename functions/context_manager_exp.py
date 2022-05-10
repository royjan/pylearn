import contextlib


@contextlib.contextmanager
def open_file(file_name: str):
    file_obj = open(file_name)
    yield file_obj, file_name
    file_obj.close()


if __name__ == '__main__':
    FILE_NAME = "file_text.txt"

    file = open(FILE_NAME)
    data = file.read().split("\n")
    file.close()
    print(data, end="\n\n")

    with open_file(FILE_NAME) as file:
        data = file.read().split("\n")
    print(data)

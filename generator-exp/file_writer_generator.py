import tempfile
from contextlib import contextmanager


def read_without_generator(_file):
    return _file.read()


def read_with_generator(_file, chunk_size=1024):
    while True:
        data = _file.read(chunk_size)
        if not data:
            break
        yield data


@contextmanager
def using_temp_file():
    temp = tempfile.TemporaryFile()
    yield temp
    temp.close()


def jump_to_start():
    file.seek(0)


if __name__ == '__main__':
    with using_temp_file() as temp_file:
        file = temp_file.file

        file.write(b"abcd" * 5)
        jump_to_start()

        print("### print with generator ###")
        for chunk in read_with_generator(file, chunk_size=4):
            print(chunk)
        jump_to_start()

        print("\n### print without generator ###")
        print(read_without_generator(file))

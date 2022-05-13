import wave
import argparse
import contextlib

from functools import wraps
from time import time


def timing(f: callable):  # https://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % (f.__name__, args, kw, te - ts))
        return result

    return wrap


def get_file_duration(file_path: str):  # https://stackoverflow.com/questions/7833807/get-wav-file-length-or-duration
    with contextlib.closing(wave.open(file_path)) as file:
        frames = file.getnframes()
        rate = file.getframerate()
        duration = frames / float(rate)
    return duration


def get_arguments():
    parser = argparse.ArgumentParser(description='Get file duration')
    parser.add_argument("-m", "--media", required=True, help="Media path", type=str)
    parser.add_argument("-ti", "--timeit", required=False, help="Time to run", action="store_true")
    return parser.parse_args()


if __name__ == '__main__':
    my_args = get_arguments()
    function = timing(get_file_duration) if my_args.timeit else get_file_duration
    duration_file = function(my_args.media)
    print(f"{my_args.media} - {duration_file} seconds")

import wave
import argparse
import contextlib

from functools import wraps
from time import time


def timing(f):  # https://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % (f.__name__, args, kw, te - ts))
        return result

    return wrap


def get_arguments():
    parser = argparse.ArgumentParser(description='Get file duration')
    parser.add_argument("-m", "--media", type=str, required=True, help="Media path")
    parser.add_argument("-ti", "--timeit", required=False, help="How much time it took", action="store_true")
    return parser.parse_args()


def get_file_duration(file_path: str):
    with contextlib.closing(wave.open(file_path)) as file:
        frames = file.getnframes()
        rate = file.getframerate()
        duration = frames / float(rate)
    return duration


if __name__ == '__main__':
    my_args = get_arguments()
    function = get_file_duration if not my_args.timeit else timing(get_file_duration)
    duration_file = function(my_args.media)
    print(duration_file)

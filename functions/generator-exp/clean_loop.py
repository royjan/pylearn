from typing import Generator


def get_even_numbers(max_number: int) -> Generator:
    for number in range(max_number):
        if number % 2 == 0:
            yield number


if __name__ == '__main__':
    for number in range(15):
        if number % 2 == 0:
            print(number)

    print()
    # vs

    for number in get_even_numbers(15):
        print(number)

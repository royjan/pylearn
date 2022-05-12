MAXIMUM_NUMBER = 1_000_000_000


def get_numbers_of_even_numbers_with_len():
    return len([num for num in range(MAXIMUM_NUMBER) if num % 2 == 0])


def get_numbers_of_even_numbers_with_sum():
    return sum(1 for num in range(MAXIMUM_NUMBER) if num % 2 == 0)


def get_numbers_of_even_numbers_with_sum2():
    return sum(num % 2 == 0 for num in range(MAXIMUM_NUMBER))

def calculate_avg():
    total_sum, counter = 0, 0
    while True:
        total_sum += yield
        counter += 1
        yield total_sum / counter


if __name__ == '__main__':
    calculator = calculate_avg()
    next(calculator)
    calculator.send(5)
    next(calculator)
    x = calculator.send(7)
    print(x)

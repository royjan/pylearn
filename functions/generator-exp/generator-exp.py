def calculate_avg():
    total_sum, counter = 0, 0
    while True:
        total_sum += yield
        counter += 1
        yield total_sum / counter


if __name__ == '__main__':
    avg_calculator = calculate_avg()
    next(avg_calculator)
    avg_calculator.send(5)
    next(avg_calculator)
    result = avg_calculator.send(7)
    print(result)
    next(avg_calculator)
    result = avg_calculator.send(21)
    print(result)  # (5+7+21)/3=11

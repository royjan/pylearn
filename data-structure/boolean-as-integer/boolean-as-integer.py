lst = [1, 2, 3, 4, 5, 6, 12, 14, 16, 21, -9, 13]



even_nums_with_sum_and_ones = sum(1 for num in lst if num % 2 == 0)
even_nums_with_len = len([num for num in lst if num % 2 == 0])
even_nums_with_sum = sum(num % 2 == 0 for num in lst)

print(even_nums_with_len)
print(even_nums_with_sum_and_ones)
print(even_nums_with_sum)

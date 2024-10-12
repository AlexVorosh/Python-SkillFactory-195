multipl = 1
for i in range(1,11):
    if i % 2 == 0:
        continue
    multipl *= i
print("Произведение всех нечетных чисел от 1 до 10 равно:", multipl)
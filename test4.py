for num in range(100,1000):
     num_str = str(num)
     if all(int(digit) % 2 == 0 for digit in num_str):
        print(num)

import numpy as np

numbers=[]
n = int(input("entr the n:"))

for i in range(n):
    number=int(input(f"Entr number{i+1}):"))
    numbers.append(number)

maximum=np.max(numbers)
minimum=np.min(numbers)
average=np.mean(numbers)
std=np.std(numbers) # standard deviation
print("Maximum is:",maximum)
print("Minimum is:",minimum)
print("Average is:",average)
print(f"Standard Deviation is: {std:.2f}")











from statistics import mean
import math


def Max1(numbers):
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    print("The Maximum is: ", max)


def Min1(numbers):
    min = numbers[0]
    for num in numbers:
        if num < min:
            min = num
    print("The Minimum is: ", min)


def Ave1(numbers):
    sum = 0
    for num in numbers:
        sum += num
    average = sum / len(numbers)
    print("The Average is: ", average)


def STD1(numbers):
    average = mean(numbers)
    sum = 0
    for num in numbers:
        sum += ((num - average) ** 2)

    std = math.sqrt(sum / len(numbers))
    print(f"The Standard Deviation is: {std:.2f}")


numbers = []
n = int(input("Enter the n:"))
for i in range(n):
    number = int(input(f"Enter number {i + 1}:"))
    numbers.append(number)

Max1(numbers)
Min1(numbers)
Ave1(numbers)
STD1(numbers)
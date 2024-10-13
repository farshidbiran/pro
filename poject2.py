import math

def computeExpression(n):
    change_sign = True
    sign = 1
    fact = 3
    first_number = 2
    second_number = 9
    result = 0
    for _ in range(n):
         fact = math.factorial(fact)
         result += sign * (fact / (first_number + second_number))
         fact += 2
         first_number += 1
         second_number -= 2
         if change_sign:
              sign = -1
              change_sign = False
         else:
              sign = 1
              change_sign = True
    return result

print(computeExpression(5))# 12is error

def F1(num):
    return max(num)

def F2(num, max):
    num = str(num)
    result = []
    for d in num:
        if d != max:
            result.append(d)
    return "".join(result)


number = input('Enter a  5 digits number: ')

while True:
    if number.isdigit() and len(number) == 5:
        maximum = F1(number)
        print(f"the final digit is: {F2(number, maximum)}")
        break
    else:
        print("It is not 5 digit number.")
        number = input('Please enter a valid number: ')

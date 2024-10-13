number=input("ENTER a number:")
even =[]
for digit in number:
    digit=int(digit)
    if digit % 2==0:
        even.append(str(digit))

print("*".join(even))

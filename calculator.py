print ("Python Basic Calculator")
print ("Please Choose the operation!")
print("1. Addition")
print("2. Subtraction")
print("3. Multiply")
print("4. Distribution")
choice = input("Your choice= ")

number1 = float(input("Input number 1 = "))
number2 = float(input("Input number 2 = "))

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def dis(a,b):
    return a/b

if choice == '1':
    print(number1, "+", number2, "=", add(number1,number2))

elif choice == '2':
    print(number1, "-", number2, "=", sub(number1,number2))

elif choice == '3':
    print(number1, "*", number2, "=", mul(number1,number2))

elif choice == '4':
    print(number1, ":", number2, "=", dis(number1,number2))

else:
    print("Error input!")


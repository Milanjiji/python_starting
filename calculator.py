import math 


print("what operation do you want to perform: \n")
print("press 1 for doing normal calcualtions eg : +,-,/,*")
print("press 2 for doing factorial")
print("press 3 for get angle ")
mainop = input("Enther the operator: ")

if mainop == "1":
    num1 = float(input("Enter the first number"))
    num2 = float(input("Enter the second number"))
    result = 0
    op = input("Enter the operator")

    if op == "+" :
        print(sum([num1,num2]))
    elif op == "-" :
        result = num1 - num2
        print(result)
    elif op == "/" :
        result = num1 / num2
        print(result)
    elif op == "*" :
        result = num1 * num2
        print(result)
    else:
        print("error")

elif mainop == "2":
    num = int(input("Enter the number to get factorial: "))
    factorial = 1
    for i in range(1,num +1):
        factorial *= i
    print(factorial)

elif mainop == "3":
    print("In which form does you want to get the ans:")
    print("press 1 for get ans in dgrees or 2 for radians")
    choise = input("Enter the option: ")

    print("What operation does you want to do ")
    
    print("press 3 to get sine of angle")
    print("press 4 to get cos of angle")
    print("press 5 to get tan of angle")
    choise2 = input("Enter the option: ")
    

    # if choise2 == "1":
    #     val = input("Enter the radian value: ")
    #     res = math.degrees(val)
    #     op2 = "1"
    # elif choise2 == "2":
    #     val = input("Enter the degree value: ")
    #     res = math.radians(val)
    #     op2 = "2"
    if choise2 == "3":
        val = int(input("Enter the angle: "))
        res = math.sin(val)
    elif choise2 == "4":
        val = int(input("Enter the angle: "))
        res = math.cos(val)
    elif choise2 == "5":
        val = int(input("Enter the angle: "))
        res = math.tan(val)
    
    if choise == "1":
       print(math.degrees(res))
    elif choise == "2":
        print(math.radians(res))

    
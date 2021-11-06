def factorial(num):
    res = 1
    for i in range(1, num+1):
        res = res* i
    print("The factorial of", num, "is: ", res)

factorial(6)
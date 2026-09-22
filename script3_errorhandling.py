def divide_numbers(a,b) :
    try :
        result = a/b
        print(result)
    except ZeroDivisionError :
        print("Error: Aap zero se divide nahi kar sakte")


divide_numbers(10, 2)
divide_numbers(10, 0)



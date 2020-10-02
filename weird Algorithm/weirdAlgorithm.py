remaing_test_cases = int(input())

while remaing_test_cases > 0:
    number = int(input())
    print(number,end=" ")
    
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number,end=" ")
        else:
            number = number * 3 + 1
            print(number,end=" ")
    print()   


    remaing_test_cases = remaing_test_cases - 1

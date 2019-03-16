
i=int(input("Enter any possitive integer between 1 and 100:"))
if i <= 1:
    print("number is not prime")
else:
    a=2
    check = True
    while a != i:
        if i%a == 0:
            print("Number is not prime")
            check = False
            break
        a+=1
    if check == True:
        print("Number is prime")
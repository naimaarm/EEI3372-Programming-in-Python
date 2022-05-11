try:
    my_list = []

    while True:
        x = int(input("Enter a price, 0 to End :"))
        if x == 0:
            break
        elif x < 0:
            print("Please enter positive Number")
        else:
            my_list.append(x)
except:
    print(my_list)

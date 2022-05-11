my_list = []
while True:
    price = input("Enter a price, 0 to End :")
    try:
        item = int(price) or float(price)
        if item < 0:
            print("Please enter a positive number")
        elif item == 0:
            break
        else:
            my_list.append(item)
    except ValueError:
        print("Please enter a number")

total = sum(my_list)
count = len(my_list)
average = total / count
max_price = max(my_list)
min_price = min(my_list)
count_havg = 0
for i in my_list:
    if i >= average:
        count_havg = count_havg + 1

count_lavg = 0
for i in my_list:
    if i < average:
        count_lavg = count_lavg + 1


print("\n\nTotal price is :", total)
print("Total number of items in list :", count)
print("Average price is :", average)
print("Highest price is :", max_price)
print("Lowest price is :", min_price)
print("# of prices >= to the average", count_havg)
print("# of prices < to the average", count_lavg)

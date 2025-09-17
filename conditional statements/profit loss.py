costprice=int(input("Enter the cost price "))
sellingprice=int(input("Enter the selling price "))

if costprice<sellingprice:
    print("profit")

elif costprice>sellingprice:
    print("loss")

else:
    print("no profit or loss")
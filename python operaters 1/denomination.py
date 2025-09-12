# to find the denomination of a given amount

amount = int(input("Enter the Amount :"))

hundred = amount // 100

amt = amount % 100

fifty = amount // 50

amt = amount % 50

ten = amount // 10

print("No of Hundred Notes :", hundred)

print("No of Fifty Notes :", fifty)

print("No of Ten Notes :", ten)
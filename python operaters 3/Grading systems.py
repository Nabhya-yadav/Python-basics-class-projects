eng=int(input("Enter the marks for English "))
math=int(input("Enter the marks for Maths "))
sci=int(input("Enter the marks for Science "))
ins=int(input("Enter the marks for I&S "))

totalmarks=eng+math+sci+ins

average=totalmarks/4

if (average>=91) and (average<=100):
    print("A")

elif (average>=81) and (average<=90):
    print("B")
elif (average>=71) and (average<=80):
    print("C")

elif (average>=61) and (average<=70):
    print("D")

elif (average>=21) and (average<=60):
    print("E")

elif (average>=0) and (average<=20):
    print("F")

else:
    print("invalid error")
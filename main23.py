a = int(input("Enter your number"))
n = int("Number of powers")
for i in range(1,n+1):
    p = a**i
    print("{0} power of {1} is{2} ".format(i,a,p))

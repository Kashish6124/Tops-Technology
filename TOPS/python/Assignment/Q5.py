#Write a Python program to get the Factorial number of given numbers

n=int(input("Enter a factorial number"))
fact=1
for i in range(1,n+1):
    fact*=i

print("Factorial is :",fact) 

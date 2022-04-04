#WAS ENTER 3 NUMBER AND PRINT WHICH NUMBER IS MAXIMUM NUMBER
no1=int(input("enter value for no1:"))
no2=int(input("enter value for no2:"))
no3=int(input("enter value for no3:"))
if(no1>no2)and(no1>no3):
    largest=no1
elif(no2>no1)and(no2>no3):
    largest=no2
else:
    largest=no3
print("{} is the largest number".format(largest))

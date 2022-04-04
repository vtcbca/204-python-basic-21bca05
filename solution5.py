#WAS TO ENTER ANY NUMBER AND PRINT FROM WHICH NUMBER FROM 0 TO 9 IT IS DIVISABLE:
no1=int(input("Enter the number to be devided by:"))
no2=1
while(no2<10):
    if(no1%no2==0):
         print("{} is divisible by {}".format(no1,no2))
    no2=no2+1

